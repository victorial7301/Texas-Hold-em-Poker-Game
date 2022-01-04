#include <assert.h>
#include <stdio.h>
#include <limits.h>
#include <stdlib.h>

#include "lib/xalloc.h"
#include "lib/stack.h"
#include "lib/contracts.h"
#include "lib/c0v_stack.h"
#include "lib/c0vm.h"
#include "lib/c0vm_c0ffi.h"
#include "lib/c0vm_abort.h"

/* call stack frames */
typedef struct frame_info frame;
struct frame_info {
  c0v_stack_t S; /* Operand stack of C0 values */
  ubyte *P;      /* Function body */
  size_t pc;     /* Program counter */
  c0_value *V;   /* The local variables */
};

int execute(struct bc0_file *bc0) {
  REQUIRES(bc0 != NULL);

  /* Variables */
  c0v_stack_t S = c0v_stack_new(); /* Operand stack of C0 values */
  ubyte *P = bc0->function_pool[0].code;      /* Array of bytes that make up the current function */
  size_t pc = 0;     /* Current location within the current byte array P */
  c0_value *V = xmalloc((bc0->function_pool[0].num_vars)*sizeof(c0_value));   /* Local variables (you won't need this till Task 2) */

  gstack_t callStack = stack_new();

  while (true) {

#ifdef DEBUG
    fprintf(stderr, "Opcode %x -- Stack size: %zu -- PC: %zu\n",
            P[pc], c0v_stack_size(S), pc);
#endif

    switch (P[pc]) {

    /* Additional stack operation: */

    case POP: {
      pc++;
      c0v_pop(S);
      break;
    }

    case DUP: {
      pc++;
      c0_value v = c0v_pop(S);
      c0v_push(S,v);
      c0v_push(S,v);
      break;
    }

    case SWAP: {
      pc++;
      c0_value a = c0v_pop(S);
      c0_value b = c0v_pop(S);
      c0v_push(S, a);
      c0v_push(S, b);
      break;
    }

    case RETURN: {
      c0_value return_value = c0v_pop(S);
      if (stack_empty(callStack)) {
      #ifdef DEBUG
      /* You can add extra debugging information here */
      fprintf(stderr, "Opcode %x -- Stack size: %zu -- PC: %zu\n",
              P[pc], c0v_stack_size(S), pc);
      #endif
      free(V); c0v_stack_free(S); 
      stack_free(callStack, NULL);
      return val2int(return_value); }
      stack_elem ptr_to_frame = pop(callStack);
      free(V); c0v_stack_free(S);
      // Restore V, S, P, and pc from the stack frame.
      V = ((frame*)ptr_to_frame)->V;
      S = ((frame*)ptr_to_frame)->S;
      P = ((frame*)ptr_to_frame)->P;
      pc = ((frame*)ptr_to_frame)->pc;
      free(ptr_to_frame);
      c0v_push(S, return_value);
      break;
    }

    /* Arithmetic and Logical operations */

    case IADD: {
      pc++;
      c0_value b = c0v_pop(S);
      c0_value a = c0v_pop(S);
      int32_t c = val2int(b) + val2int(a);
      c0v_push(S, int2val(c));
      break;
    }

    case ISUB: {
      pc++;
      c0_value b = c0v_pop(S);
      c0_value a = c0v_pop(S);
      int32_t c = val2int(a) - val2int(b);
      c0v_push(S, int2val(c));
      break;
    }

    case IMUL: {
      pc++;
      c0_value b = c0v_pop(S);
      c0_value a = c0v_pop(S);
      int32_t c = val2int(a)*val2int(b);
      c0v_push(S, int2val(c));
      break;
    }

    case IDIV: {
      pc++;
      c0_value b = c0v_pop(S);
      c0_value a = c0v_pop(S);
      if (val2int(b) == 0) c0_arith_error("You can't divide by zero.");
      else if (val2int(a) == INT_MIN && val2int(b) == -1) {
        c0_arith_error("Overflow error");
      }
      else {
        int32_t c = val2int(a)/val2int(b);
        c0v_push(S, int2val(c));
      }
      break;
    }

    case IREM: {
      pc++;
      c0_value b = c0v_pop(S);
      c0_value a = c0v_pop(S);
      if (val2int(b) == 0) c0_arith_error("You can't mod by zero.");
      else if (val2int(a) == INT_MIN && val2int(b) == -1) {
        c0_arith_error("Overflow error");
      }
      else {
        int32_t c = val2int(a)%val2int(b);
        c0v_push(S, int2val(c));
      }
      break;
    }

    case IAND: {
      pc++;
      c0_value b = c0v_pop(S);
      c0_value a = c0v_pop(S);
      int32_t c = val2int(a) & val2int(b);
      c0v_push(S, int2val(c));
      break;
    }

    case IOR: {
      pc++;
      c0_value b = c0v_pop(S);
      c0_value a = c0v_pop(S);
      int32_t c = val2int(a) | val2int(b);
      c0v_push(S, int2val(c));
      break;
    }

    case IXOR: {
      pc++;
      c0_value b = c0v_pop(S);
      c0_value a = c0v_pop(S);
      int32_t c = val2int(a) ^ val2int(b);
      c0v_push(S, int2val(c));
      break;
    }

    case ISHL: {
      pc++;
      c0_value b = c0v_pop(S);
      c0_value a = c0v_pop(S);
      if (val2int(b) > 31 || val2int(b) < 0) {
        char *err = "You can't shift more than 31 or less than 0.";
        c0_arith_error(err);
      }
      int32_t c = val2int(a) << val2int(b);
      c0v_push(S, int2val(c));
      break;
    }

    case ISHR: {
      pc++;
      c0_value b = c0v_pop(S);
      c0_value a = c0v_pop(S);
      if (val2int(b) > 31 || val2int(b) < 0) {
        char *err = "You can't shift more than 31 or less than 0.";
        c0_arith_error(err);
      }
      int32_t c = val2int(a) >> val2int(b);
      c0v_push(S, int2val(c));
      break;
    }

    /* Pushing constants */

    case BIPUSH: {
      pc++;
      c0v_push(S, int2val((int32_t)(int8_t)P[pc]));
      pc++;
      break;
    }

    case ILDC: {
      pc++;
      uint16_t index = (uint16_t)(P[pc]) << 8;
      pc++;
      index = index | (uint16_t)(P[pc]);
      c0v_push(S, int2val(bc0->int_pool[index]));
      pc++;
      break;
    }

    case ALDC: {
      pc++;
      uint16_t index = (uint16_t)(P[pc]) << 8;
      pc++;
      index = index | (uint16_t)(P[pc]);
      void* ptr = (void*)(&(bc0->string_pool[index]));
      c0v_push(S, ptr2val(ptr));
      pc++;
      break;
    }

    case ACONST_NULL: {
      pc++;
      c0v_push(S, ptr2val(NULL));
      break;
    }

    /* Operations on local variables */

    case VLOAD: {
      pc++;
      c0_value var = V[P[pc]];
      c0v_push(S, var);
      pc++;
      break;
    }

    case VSTORE: {
      pc++;
      c0_value var = c0v_pop(S);
      V[P[pc]] = var;
      pc++;
      break;
    }

    /* Assertions and errors */

    case ATHROW: {
      pc++;
      c0_value error = c0v_pop(S);
      c0_user_error((char*)val2ptr(error));
      break;
    }

    case ASSERT: {
      pc++;
      c0_value a = c0v_pop(S);
      c0_value x = c0v_pop(S);
      if (val2int(x) == 0) {
        c0_assertion_failure((char*)val2ptr(a));
      }
      break;
    }

    /* Control flow operations */

    case NOP: {
      pc++;
      break;
    }

    case IF_CMPEQ: {
      c0_value b = c0v_pop(S);
      c0_value a = c0v_pop(S);
      if (val_equal(a, b)) {
        pc++;
        int16_t change = ((int16_t)(int8_t)(P[pc])) << 8;
        pc++;
        change = change | (int16_t)(uint16_t)(P[pc]);
        pc = pc - 2 + change; 
      }
      else pc += 3;
      break;
    }

    case IF_CMPNE: {
      c0_value b = c0v_pop(S);
      c0_value a = c0v_pop(S);
      if (!val_equal(a, b)) {
        pc++;
        int16_t change = ((int16_t)(int8_t)(P[pc])) << 8;
        pc++;
        change = change | (int16_t)(uint16_t)(P[pc]);
        pc = pc - 2 + change; 
      }
      else pc += 3;
      break;
    }

    case IF_ICMPLT: {
      c0_value b = c0v_pop(S);
      c0_value a = c0v_pop(S);
      if (val2int(a) < val2int(b)) {
        pc++;
        int16_t change = ((int16_t)(int8_t)(P[pc])) << 8;
        pc++;
        change = change | (int16_t)(uint16_t)(P[pc]);
        pc = pc - 2 + change; 
      }
      else pc += 3;
      break;
    }

    case IF_ICMPGE: {
      c0_value b = c0v_pop(S);
      c0_value a = c0v_pop(S);
      if (val2int(a) >= val2int(b)) {
        pc++;
        int16_t change = ((int16_t)(int8_t)(P[pc])) << 8;
        pc++;
        change = change | (int16_t)(uint16_t)(P[pc]);
        pc = pc - 2 + change; 
      }
      else pc += 3;
      break;
    }

    case IF_ICMPGT: {
      c0_value b = c0v_pop(S);
      c0_value a = c0v_pop(S);
      if (val2int(a) > val2int(b)) {
        pc++;
        int16_t change = ((int16_t)(int8_t)(P[pc])) << 8;
        pc++;
        change = change | (int16_t)(uint16_t)(P[pc]);
        pc = pc - 2 + change; 
      }
      else pc += 3;
      break;
    }

    case IF_ICMPLE: {
      c0_value b = c0v_pop(S);
      c0_value a = c0v_pop(S);
      if (val2int(a) <= val2int(b)) {
        pc++;
        int16_t change = ((int16_t)(int8_t)(P[pc])) << 8;
        pc++;
        change = change | (int16_t)(uint16_t)(P[pc]);
        pc = pc - 2 + change; 
      }
      else pc += 3;
      break;
    }

    case GOTO: {
      pc++;
      int16_t change = ((int16_t)(int8_t)(P[pc])) << 8;
      pc++;
      change = change | (int16_t)(uint16_t)(P[pc]);
      pc = pc - 2 + change; 
      break;
    }

    /* Function call operations: */

    case INVOKESTATIC: {
      frame* F = xmalloc(sizeof(frame));
      F->P = P;
      F->pc = pc + 3;
      F->V = V;
      F->S = S;
      push(callStack, (stack_elem)F);
      pc++;
      uint16_t index = (uint16_t)(P[pc]) << 8;
      pc++;
      index = index | (uint16_t)(P[pc]);
      V = xmalloc((bc0->function_pool[index].num_vars)*sizeof(c0_value));
      uint8_t arg_num = bc0->function_pool[index].num_args;
      for (uint8_t i = 0; i < arg_num; i++) {
        V[arg_num - 1 - i] = c0v_pop(S);
      }
      S = c0v_stack_new();
      P = bc0->function_pool[index].code;
      pc = 0;
      break;
    }
      
    case INVOKENATIVE: {
      pc++;
      uint16_t index = (uint16_t)(P[pc]) << 8;
      pc++;
      index = index | (uint16_t)(P[pc]);
      uint8_t arg_num = bc0->native_pool[index].num_args;
      c0_value *V_new = xmalloc(arg_num*sizeof(c0_value));
      for (uint16_t i = 0; i < arg_num; i++) {
        V_new[arg_num - 1 - i] = c0v_pop(S); // index right?
      }
      uint16_t table_index = bc0->native_pool[index].function_table_index;
      c0_value result = (*native_function_table[table_index])(V_new);
      c0v_push(S, result);
      free(V_new);
      pc++;
      break;
    }

    /* Memory allocation operations: */
    
    case NEW: {
      pc++;
      void *ptr = xmalloc(sizeof(P[pc]));
      c0v_push(S, ptr2val(ptr));
      pc++;
      break;
    }

    case NEWARRAY: {
      pc++;
      int32_t count = val2int(c0v_pop(S));
      if (count == 0) {
        c0_array* array = NULL;
        c0v_push(S, ptr2val(array));
      }
      else {
        c0_array* array = xmalloc(sizeof(c0_array));
        array->count = count;
        array->elt_size = P[pc]; 
        array->elems = xcalloc(count, P[pc]);
        c0v_push(S, ptr2val((void*)array));
      }
      pc++;
      break;
    }

    case ARRAYLENGTH: {
      pc++;
      void *ptr = val2ptr(c0v_pop(S));
      int32_t count = ((c0_array*)ptr)->count;
      c0v_push(S, int2val(count));
      break;
    }
  
    /* Memory access operations: */
    
    case AADDF: {
      pc++;
      c0_value ptr = c0v_pop(S);
      char *err = "a can't be NULL.";
      if (val2ptr(ptr) == NULL) c0_memory_error(err);
      else {
        ubyte *p = val2ptr(ptr);
        p += P[pc];
        c0v_push(S, ptr2val((void*)p));
      }
      pc++;
      break;
    }

    case AADDS: {
      pc++;
      int32_t integer = val2int(c0v_pop(S));
      void *ptr = val2ptr(c0v_pop(S));
      int32_t array_length = ((c0_array*)ptr)->count;
      char *err = "a can't be NULL and the array length must be correct.";
      if (ptr == NULL || 0 > integer || integer >= array_length) {
        c0_memory_error(err);
      }
      else {
        int32_t size = ((c0_array*)ptr)->elt_size;
        ubyte *array_elem = (ubyte*)(((c0_array*)ptr)->elems) + size*integer;
        c0v_push(S, ptr2val((void*)array_elem));
      }
      break;
    }

    case IMLOAD: {
      pc++;
      c0_value ptr = c0v_pop(S);
      char *err = "a can't be NULL.";
      if (val2ptr(ptr) == NULL) c0_memory_error(err);
      else {
        int32_t integer = *((int32_t*)(val2ptr(ptr)));
        c0v_push(S, int2val(integer));
      }
      break;
    }

    case IMSTORE: {
      pc++;
      c0_value integer = c0v_pop(S);
      c0_value ptr  = c0v_pop(S);
      char *err = "a can't be NULL.";
      if (val2ptr(ptr) == NULL) c0_memory_error(err);
      else {
        *((int32_t*)(val2ptr(ptr))) = val2int(integer);
      }
      break;
    }

    case AMLOAD: {
      pc++;
      c0_value ptr = c0v_pop(S);
      char *err = "a can't be NULL.";
      if (val2ptr(ptr) == NULL) c0_memory_error(err);
      else {
        void *ptr2 = *((void**)(val2ptr(ptr)));
        c0v_push(S, ptr2val(ptr2));
      }
      break;
    }

    case AMSTORE: {
      pc++;
      c0_value ptr = c0v_pop(S);
      c0_value ptr2 = c0v_pop(S);
      char *err = "a can't be NULL.";
      if (val2ptr(ptr2) == NULL) c0_memory_error(err);
      else {
        *((void**)(val2ptr(ptr2))) = val2ptr(ptr);
      }
      break;
    }

    case CMLOAD: {
      pc++;
      c0_value ptr = c0v_pop(S);
      char *err = "a can't be NULL.";
      if (val2ptr(ptr) == NULL) c0_memory_error(err);
      else {
        int32_t integer = (int32_t)(uint32_t)*((char*)val2ptr(ptr));
        c0v_push(S, int2val(integer));
      }
      break;
    }

    case CMSTORE: {
      pc++;
      c0_value integer = c0v_pop(S);
      c0_value ptr = c0v_pop(S);
      char *err = "a can't be NULL.";
      if (val2ptr(ptr) == NULL) c0_memory_error(err);
      else {
        *((char*)val2ptr(ptr)) = val2int(integer) & 0x7f;
      }
      break;
    }

    default:
      fprintf(stderr, "invalid opcode: 0x%02x\n", P[pc]);
      abort();
    }
  }
  /* cannot get here from infinite loop */
  assert(false);
}
