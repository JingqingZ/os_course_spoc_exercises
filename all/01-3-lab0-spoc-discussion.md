# lab0 SPOC思考题

## 分析和实验funcall.c，需要完成的内容包括：

### 修改代码，可正常显示小组两位同学的学号（用字符串）
```c
#include <u.h>
int ret;
out(port, val)
{
  asm(LL,8);   // load register a with port
  asm(LBL,16); // load register b with val
  asm(BOUT);   // output byte to console
}
##**提前准备**
（请在上课前完成）

 - 完成lec2的视频学习和提交对应的在线练习
 - git pull ucore_os_lab, v9_cpu, os_course_spoc_exercises  　in github repos。这样可以在本机上完成课堂练习。
 - 了解代码段，数据段，执行文件，执行文件格式，堆，栈，控制流，函数调用,函数参数传递，用户态（用户模式），内核态（内核模式）等基本概念。思考一下这些基本概念在linux, ucore, v9-cpu中的os*.c中是如何具体体现的。
 - 安装好ucore实验环境，能够编译运行ucore labs中的源码。
 - 会使用linux中的shell命令:objdump，nm，file, strace，gdb等，了解这些命令的用途。
 - 会编译，运行，使用v9-cpu的dis,xc, xem命令（包括启动参数），阅读v9-cpu中的cpu.md文档，了解汇编指令的类型和含义等，了解v9-cpu的细节。如能debug dis, xc, xem更佳。
 - 了解基于v9-cpu的执行文件的格式和内容，以及它是如何加载到v9-cpu的内存中的。
 - 在piazza上就学习中不理解问题进行提问。

## 个人思考题

---

能否读懂ucore中的AT&T格式的X86-32汇编语言？请列出你不理解的汇编语言。
- [x]

>  http://www.imada.sdu.dk/Courses/DM18/Litteratur/IntelnATT.htm
>  inb一般应用程序用不到的指令等。

虽然学过计算机原理和x86汇编（根据THU-CS的课程设置），但对ucore中涉及的哪些硬件设计或功能细节不够了解？
- [x]

> 中断寄存器和非通用寄存器等。


哪些困难（请分优先级）会阻碍你自主完成lab实验？
- [x]

>

如何把一个在gdb中或执行过程中出现的物理/线性地址与你写的代码源码位置对应起来？
- [x]

> 1. 在gdb中通过break加行号得到物理地址，list加*物理地址得到行号。
> 2. 用nm, objdump工具可以看到

了解函数调用栈对lab实验有何帮助？
- [x]

> 除了错可以调试
> 对于函数的调用过程和程序的运行过程有更好的理解。
> 便于调试以及检查。

你希望从lab中学到什么知识？
- [x]

>

---

## 小组讨论题

---

搭建好实验环境，请描述碰到的困难和解决的过程。
- [x]

> 困难：在virtualbox中设置虚拟机的时候找不到Linux的64位选项。
> 解决：需要通过BIOS设置将电脑的虚拟化功能打开（本电脑LenovoY480的VT功能是锁的，需要打开）。
> 开始时选择了UBUNTU 32位，不能启动，后来换成64位就能顺利运行

熟悉基本的git命令行操作命令，从github上
的 http://www.github.com/chyyuu/ucore_lab 下载
ucore lab实验
- [x]

> clone 仓库
> gitclone http://www.github.com/chyyuu/ucore_lab

尝试用qemu+gdb（or ECLIPSE-CDT）调试lab1
- [x]

> 清除文件夹：make clean
> 编译lab1：make
> 调出debug命令行：make debug

int write(int f, char *s, int n)
{
  int i;
  ret = 1;
  i=n;
  while (i--)
    out(f, *s++);
  return i;
}

main()
{

  //Change S1/S2 ID to your student ID, and change 12 to new str length
  ret = write(1, "2012011380 2012011297", 21);
  asm(HALT);
}
```

### 生成funcall.c的汇编码，理解其实现并给汇编码写注释
```c
root/usr/funcall.c  1: #include <u.h>
root/lib/u.h  1: // u.h
root/lib/u.h  2:
root/lib/u.h  3: // instruction set
root/lib/u.h  4: enum {
root/lib/u.h  5:   HALT,ENT ,LEV ,JMP ,JMPI,JSR ,JSRA,LEA ,LEAG,CYC ,MCPY,MCMP,MCHR,MSET, // system
root/lib/u.h  6:   LL  ,LLS ,LLH ,LLC ,LLB ,LLD ,LLF ,LG  ,LGS ,LGH ,LGC ,LGB ,LGD ,LGF , // load a
root/lib/u.h  7:   LX  ,LXS ,LXH ,LXC ,LXB ,LXD ,LXF ,LI  ,LHI ,LIF ,
root/lib/u.h  8:   LBL ,LBLS,LBLH,LBLC,LBLB,LBLD,LBLF,LBG ,LBGS,LBGH,LBGC,LBGB,LBGD,LBGF, // load b
root/lib/u.h  9:   LBX ,LBXS,LBXH,LBXC,LBXB,LBXD,LBXF,LBI ,LBHI,LBIF,LBA ,LBAD,
root/lib/u.h  10:   SL  ,SLH ,SLB ,SLD ,SLF ,SG  ,SGH ,SGB ,SGD ,SGF ,                     // store
root/lib/u.h  11:   SX  ,SXH ,SXB ,SXD ,SXF ,
root/lib/u.h  12:   ADDF,SUBF,MULF,DIVF,                                                   // arithmetic
root/lib/u.h  13:   ADD ,ADDI,ADDL,SUB ,SUBI,SUBL,MUL ,MULI,MULL,DIV ,DIVI,DIVL,
root/lib/u.h  14:   DVU ,DVUI,DVUL,MOD ,MODI,MODL,MDU ,MDUI,MDUL,AND ,ANDI,ANDL,
root/lib/u.h  15:   OR  ,ORI ,ORL ,XOR ,XORI,XORL,SHL ,SHLI,SHLL,SHR ,SHRI,SHRL,
root/lib/u.h  16:   SRU ,SRUI,SRUL,EQ  ,EQF ,NE  ,NEF ,LT  ,LTU ,LTF ,GE  ,GEU ,GEF ,      // logical
root/lib/u.h  17:   BZ  ,BZF ,BNZ ,BNZF,BE  ,BEF ,BNE ,BNEF,BLT ,BLTU,BLTF,BGE ,BGEU,BGEF, // conditional
root/lib/u.h  18:   CID ,CUD ,CDI ,CDU ,                                                   // conversion
root/lib/u.h  19:   CLI ,STI ,RTI ,BIN ,BOUT,NOP ,SSP ,PSHA,PSHI,PSHF,PSHB,POPB,POPF,POPA, // misc
root/lib/u.h  20:   IVEC,PDIR,SPAG,TIME,LVAD,TRAP,LUSP,SUSP,LCL ,LCA ,PSHC,POPC,MSIZ,
root/lib/u.h  21:   PSHG,POPG,NET1,NET2,NET3,NET4,NET5,NET6,NET7,NET8,NET9,
root/lib/u.h  22:   POW ,ATN2,FABS,ATAN,LOG ,LOGT,EXP ,FLOR,CEIL,HYPO,SIN ,COS ,TAN ,ASIN, // math
root/lib/u.h  23:   ACOS,SINH,COSH,TANH,SQRT,FMOD,
root/lib/u.h  24:   IDLE
root/lib/u.h  25: };
root/lib/u.h  26:
root/lib/u.h  27: // system calls
root/lib/u.h  28: enum {
root/lib/u.h  29:   S_fork=1, S_exit,   S_wait,   S_pipe,   S_write,  S_read,   S_close,  S_kill,
root/lib/u.h  30:   S_exec,   S_open,   S_mknod,  S_unlink, S_fstat,  S_link,   S_mkdir,  S_chdir,
root/lib/u.h  31:   S_dup2,   S_getpid, S_sbrk,   S_sleep,  S_uptime, S_lseek,  S_mount,  S_umount,
root/lib/u.h  32:   S_socket, S_bind,   S_listen, S_poll,   S_accept, S_connect,
root/lib/u.h  33: };
root/lib/u.h  34:
root/lib/u.h  35: typedef unsigned char uchar;
root/lib/u.h  36: typedef unsigned short ushort;
root/lib/u.h  37: typedef unsigned int uint;
root/lib/u.h  38:
root/usr/funcall.c  2: int ret;
root/usr/funcall.c  3: out(port, val)
root/usr/funcall.c  4: {
root/usr/funcall.c  5:   asm(LL,8);   // load register a with port
00000000  0000080e  LL    8     // a = *(sp + 8)
root/usr/funcall.c  6:   asm(LBL,16); // load register b with val
00000004  00001026  LBL   16    // b = *(sp + 16)
root/usr/funcall.c  7:   asm(BOUT);   // output byte to console
00000008  0000009a  BOUT  // output
root/usr/funcall.c  8: }
root/usr/funcall.c  9:
root/usr/funcall.c  10: int write(int f, char *s, int n)
0000000c  00000002  LEV   0
root/usr/funcall.c  11: {
root/usr/funcall.c  12:   int i;
root/usr/funcall.c  13:   ret = 1;
00000010  fffff801  ENT   0xfffffff8 (D -8)   // sp -= 8
00000014  00000123  LI    0x1 (D 1)       // a = 1
00000018  00000045  SG    0x0 (D 0)       // *(pc + 0) = a
root/usr/funcall.c  14:   i=n;
0000001c  0000200e  LL    0x20 (D 32)     // a = *(32 + sp), that is var n = *(32+sp)
00000020  00000440  SL    0x4 (D 4)       // *(4 + sp) = a, which means var i located in (4 + sp)
root/usr/funcall.c  15:   while (i--)
00000024  00000003  JMP   <fwd>
root/usr/funcall.c  16:     out(f, *s++);
00000028  0000180e  LL    0x18 (D 24)     // a = *(24 + sp)
0000002c  ffffff57  SUBI  0xffffffff (D -1)   // a -= -1
00000030  00001840  SL    0x18 (D 24)     // *(24 + sp) = a
00000034  ffffff1f  LXC   0xffffffff (D -1)   // a = *(-1)
00000038  0000009d  PSHA            //  sp -= 8, *sp = a
0000003c  0000180e  LL    0x18 (D 24)     // a = *(24 + sp)
00000040  0000009d  PSHA            //  sp -= 8, *sp = a
00000044  ffffb805  JSR   0xffffffb8 (TO 0x0) // *sp=pc, sp -= 8 and jump
00000048  00001001  ENT   0x10 (D 16)     // sp += 16
root/usr/funcall.c  17:   return i;
0000004c  0000040e  LL    4
00000050  00000157  SUBI  1
00000054  00000440  SL    4
00000058  00000154  ADDI  1
0000005c  00000086  BNZ   <fwd>
00000060  0000040e  LL    4
00000064  00000802  LEV   8
root/usr/funcall.c  18: }
root/usr/funcall.c  19:
root/usr/funcall.c  20: main()
00000068  00000802  LEV   8 // pc= *sp, sp += 8
root/usr/funcall.c  21: {
root/usr/funcall.c  22:
root/usr/funcall.c  23:   //Change S1/S2 ID to your student ID, and change 12 to new str length
root/usr/funcall.c  24:   ret = write(1, "2012011380 2012011297" , 21);
0000006c  0000159e  PSHI  21 // sp -= 8, *sp = 21, 21 is the length
00000070  00000008  LEAG  0 // a = sp/pc + 0
00000074  0000009d  PSHA    // sp -= 8, *sp = a
00000078  0000019e  PSHI  1 // store 1
0000007c  ffff9005  JSR   -112  // *sp=pc, sp -= 8, jump
00000080  00001801  ENT   24 // sp += 24
00000084  00000045  SG    0 // *(pc + 0) = a
root/usr/funcall.c  25:   asm(HALT);
00000088  00000000  HALT
root/usr/funcall.c  26: }
root/usr/funcall.c  27:
0000008c  00000002  LEV   0 //  pc = *sp, sp += 8,
```

### 尝试用xem的简单调试功能单步调试代码
```
./xem -g funcall
```

### funcall中的堆栈有多大？是内核态堆栈还是用户态堆栈
> 128M内存-4M文件系统-186Bytes代码长度 = 堆栈大小，内核态

### funcall中的全局变量ret放在内存中何处？如何对它寻址？
> 存放在代码和字符串之后0xa8，通过pc访问内存

### funcall中的字符串放在内存中何处？如何对它寻址？
> 存放在代码之后0x90，通过pc访问

### 局部变量i在内存中的何处？如何对它寻址？
> 存在堆栈中，sp+4

### 当前系统是处于中断使能状态吗？
> 不是

### funcall中的函数参数是如何传递的？函数返回值是如何传递的？
> 压入堆栈中，通过sp+8等寻址访问，返回值存到寄存器a中

### 分析并说明funcall执行文件的格式和内容　
> 首先hdr信息，然后是代码、常用数据、全局变量
### 提前准备
```
sudo apt-get install hexedit
cd YOUR v9-cpu DIR
git pull
cd YOUR os_course_spoc_exercise DIR
git pull
```

分析和实验funcall.c，需要完成的内容包括：
-[X]

 - 修改代码，可正常显示小组两位同学的学号（用字符串）
 - 生成funcall.c的汇编码，理解其实现并给汇编码写注释
 - 尝试用xem的简单调试功能单步调试代码
 - 回答如下问题：
   - funcall中的堆栈有多大？是内核态堆栈还是用户态堆栈
   - funcall中的全局变量ret放在内存中何处？如何对它寻址？
   - funcall中的字符串放在内存中何处？如何对它寻址？
   - 局部变量i在内存中的何处？如何对它寻址？
   - 当前系统是处于中断使能状态吗？
   - funcall中的函数参数是如何传递的？函数返回值是如何传递的？
   - 分析并说明funcall执行文件的格式和内容
　

分析和实验os0.c，需要完成的内容包括：
-[X]

## 分析和实验os0.c，需要完成的内容包括：
 - 生成os0.c的汇编码，理解其实现并给汇编码写注释
 - 尝试用xem的简单调试功能单步调试代码
 - 回答如下问题：
   - 何处设置的中断使能？
   - 系统何时处于中断屏蔽状态？
   - 如果系统处于中断屏蔽状态，如何让其中断使能？
   - 系统产生中断后，CPU会做哪些事情？（在没有软件帮助的情况下）
   - CPU执行RTI指令的具体完成工作是哪些？

## [HARD]分析和实验os1/os3.c，需要完成的内容包括：
 - os1中的task1和task2的堆栈的起始和终止地址是什么？
 - os1是如何实现任务切换的？
 - os3中的task1和task2的栈的起始和终止地址是什么？
 - os3是如何实现任务切换的？
 - os3的用户态task能够破坏内核态的系统吗？
