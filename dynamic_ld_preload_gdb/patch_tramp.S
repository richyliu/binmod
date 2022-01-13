.intel_syntax noprefix

.global patched_tramp

patched_tramp:
    // put any overwritten code here

    push rax
    push rbx
    push rcx
    push rdx
    push rsi
    push rdi
    push r8
    push r9
    push r10
    push r11
    push r12
    push r13
    push r14
    push r15
    push rbp

    // args = rdi, rsi, rdx, rcx, r8, r9
    // modify input registers

    // make rsp 16 byte aligned per System V ABI
    // ebx will store what we subtracted from rsp
    // ebx is callee saved, so we can be sure it stays intact
    xor ebx, ebx
    // tests whether rsp does not end in 8
    test spl, 8
    je after
    // rsp ends in 8, subtract by 8 to align it
    mov ebx, 8
after:
    sub rsp, rbx

    call patched

    // restore rsp
    add rsp, rbx

    // return = rax
    // modify return registers if needed

    pop rbp
    pop r15
    pop r14
    pop r13
    pop r12
    pop r11
    pop r10
    pop r9
    pop r8
    pop rdi
    pop rsi
    pop rdx
    pop rcx
    pop rbx
    // return value in rax, so don't pop it
    // pop rax
    add rsp, 8

    ret
