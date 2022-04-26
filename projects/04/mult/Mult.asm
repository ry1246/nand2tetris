// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

    @2
    M = 0

    @0
    D = M
    @END
    D;JLT
(LOOP)
    @1
    M = M - 1
    D = M
    @END
    D;JLT

    @0
    D = M
    @2
    M = M + D

    @LOOP
    0;JMP
(END)
    @END
    D;JMP