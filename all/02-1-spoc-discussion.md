#lec 3 SPOC Discussion

##**提前准备**
（请在周一上课前完成）

 - 完成lec3的视频学习和提交对应的在线练习
 - git pull ucore_os_lab, v9_cpu, os_course_spoc_exercises  　in github repos。这样可以在本机上完成课堂练习。
 - 仔细观察自己使用的计算机的启动过程和linux/ucore操作系统运行后的情况。搜索“80386　开机　启动”
 - 了解控制流，异常控制流，函数调用,中断，异常(故障)，系统调用（陷阱）,切换，用户态（用户模式），内核态（内核模式）等基本概念。思考一下这些基本概念在linux, ucore, v9-cpu中的os*.c中是如何具体体现的。
 - 思考为什么操作系统需要处理中断，异常，系统调用。这些是必须要有的吗？有哪些好处？有哪些不好的地方？
 - 了解在PC机上有啥中断和异常。搜索“80386　中断　异常”
 - 安装好ucore实验环境，能够编译运行lab8的answer
 - 了解Linux和ucore有哪些系统调用。搜索“linux 系统调用", 搜索lab8中的syscall关键字相关内容。在linux下执行命令: ```man syscalls```
 - 会使用linux中的命令:objdump，nm，file, strace，man, 了解这些命令的用途。
 - 了解如何OS是如何实现中断，异常，或系统调用的。会使用v9-cpu的dis,xc, xem命令（包括启动参数），分析v9-cpu中的os0.c, os2.c，了解与异常，中断，系统调用相关的os设计实现。阅读v9-cpu中的cpu.md文档，了解汇编指令的类型和含义等，了解v9-cpu的细节。
 - 在piazza上就lec3学习中不理解问题进行提问。

## 第三讲 启动、中断、异常和系统调用-思考题

## 3.1 BIOS
 1. 比较UEFI和BIOS的区别。
 > UEFI是多家公司提出的统一可扩展固件接口，BIOS相对传统
 > UEFI功能更加丰富，如图形化界面、多种多样的操作方式、允许植入硬件驱动
 > UEFI本身相当于一个微型的操作系统，而BIOS只是一个简单的启动程序
 > UEFI已具备文件系统的支持，它能够直接读取FAT分区中的文件
 > 可开发出直接在UEFI下运行的应用程序
 > UEFI硬件可与BIOS结合使用
 > UEFI通过保护预启动或预引导进程，抵御bootkit攻击，从而提高安全性
 > UEFI支持64位的现代固件设备驱动程序

 2. 描述PXE的大致启动流程。
 > 1. BIOS 启动并确定引导顺序
 > 2. 如果引导顺序将PXE放在硬盘、闪存驱动器、或CD-ROM之前，或者不存在这些设备，将从NIC加载通用网络驱动程序接口(UNDI)
 > 3. 系统执行一个简单的用户数据报协议(UDP)广播，以查找DHCP服务器
 > 4. 如果DHCP服务器听到广播，它将使用IP地址来做出相应的响应
 > 5. 系统收到DHCP服务器回应后，则会响应一个FRAME，以请求传送启动文件，之后，服务端将和客户机再进行一系列应答，以决定启动的一些参数
 > 6. 客户端通过TFTP通讯协议从服务器下载开机启动文件，启动文件接收完成后，将控制权转交给启动块，完成PXE启动

## 3.2 系统启动流程
 1. 了解NTLDR的启动流程。
 > 1. 访问启动盘的文件系统
 > 2. 如果Windows系统处在休眠状态，则读取hiberfil.sys到内存，然后系统从休眠前的状态继续
 > 3. 否则，读取boot.ini到内存，进入启动菜单
 > 4. 如果系统不是NT-based OS，则读取boot.ini或者bootsect.dos制定的文件，并把控制权交给它
 > 5. 如果系统是NT-based OS，则运行ntdetect.com检查硬件
 > 6. 运行ntoskrnl.exe并把结果返回给ntdetect.com，引导过程结束

 2. 了解GRUB的启动流程。
 > 1. BIOS启动，读取硬盘主引导扇区
 > 2. 装载stage1 stage1.5 stage2，读取grub.conf启动菜单
 > 3. 装载所选kernel和initrd文件到内存
 > 4. 运行内核启动参数，挂载文件系统，检查文件挂在系统

 3. 比较NTLDR和GRUB的功能有差异。
 4. 了解u-boot的功能。

## 3.3 中断、异常和系统调用比较
 1. 什么是中断、异常和系统调用？
 2. 中断、异常和系统调用的处理流程有什么异同？
 3. 举例说明Linux中有哪些中断，哪些异常？
 3. 以ucore lab8的answer为例，uCore的时钟中断处理流程。
 4. Linux的系统调用有哪些？大致的功能分类有哪些？  (w2l1)

 ```
  + 采分点：说明了Linux的大致数量（上百个），说明了Linux系统调用的主要分类（文件操作，进程管理，内存管理等）
  - 答案没有涉及上述两个要点；（0分）
  - 答案对上述两个要点中的某一个要点进行了正确阐述（1分）
  - 答案对上述两个要点进行了正确阐述（2分）
  - 答案除了对上述两个要点都进行了正确阐述外，还进行了扩展和更丰富的说明（3分）
 ```
 
 5. 以ucore lab8的answer为例，uCore的系统调用有哪些？大致的功能分类有哪些？(w2l1)
 
 ```
  + 采分点：说明了ucore的大致数量（二十几个），说明了ucore系统调用的主要分类（文件操作，进程管理，内存管理等）
  - 答案没有涉及上述两个要点；（0分）
  - 答案对上述两个要点中的某一个要点进行了正确阐述（1分）
  - 答案对上述两个要点进行了正确阐述（2分）
  - 答案除了对上述两个要点都进行了正确阐述外，还进行了扩展和更丰富的说明（3分）
 ```
 
## 3.4 linux系统调用分析
 1. 通过分析[lab1_ex0](https://github.com/chyyuu/ucore_lab/blob/master/related_info/lab1/lab1-ex0.md)了解Linux应用的系统调用编写和含义。(w2l1)
 > objdump是反汇编目标文件或者可执行文件的命令
 > nm显示指定文件中符号的信息，文件可以是对象文件、可执行文件或对象文件库
 > file查看文件类型
 > 系统调用时应用程序需要使用操作系统提供的服务时（如输入输出），使用系统API实现相应功能，在此过程中控制权将交给系统，进入内核态，切换到内核堆栈，拥有更多特权

 ```
  + 采分点：说明了objdump，nm，file的大致用途，说明了系统调用的具体含义
  - 答案没有涉及上述两个要点；（0分）
  - 答案对上述两个要点中的某一个要点进行了正确阐述（1分）
  - 答案对上述两个要点进行了正确阐述（2分）
  - 答案除了对上述两个要点都进行了正确阐述外，还进行了扩展和更丰富的说明（3分）
 
 ```
 
 2. 通过调试[lab1_ex1](https://github.com/chyyuu/ucore_lab/blob/master/related_info/lab1/lab1-ex1.md)了解Linux应用的系统调用执行过程。(w2l1)
 > strace可以跟踪进程执行时的系统调用和所接收的信号，strace可以跟踪到一个进程产生的系统调用,包括参数，返回值，执行消耗的时间
 > 1. 应用调用系统API，触发系统调用
 > 2. 操作系统接管控制权，堆栈切换到内核堆栈，切换到内核态，执行指定的系统调用
 > 3. 使用相应的硬件，完成相应功能
 > 4. 返回应用程序，堆栈切换回去，恢复程序执行状态

 ```
  + 采分点：说明了strace的大致用途，说明了系统调用的具体执行过程（包括应用，CPU硬件，操作系统的执行过程）
  - 答案没有涉及上述两个要点；（0分）
  - 答案对上述两个要点中的某一个要点进行了正确阐述（1分）
  - 答案对上述两个要点进行了正确阐述（2分）
  - 答案除了对上述两个要点都进行了正确阐述外，还进行了扩展和更丰富的说明（3分）
 ```
 
## 3.5 ucore系统调用分析
 1. ucore的系统调用中参数传递代码分析。
 ```c
  void
  syscall(void) {
      struct trapframe *tf = current->tf;
      uint32_t arg[5];
      int num = tf->tf_regs.reg_eax;
      if (num >= 0 && num < NUM_SYSCALLS) {
          if (syscalls[num] != NULL) {
              // 寄存器之前都已入堆栈，读取堆栈中的参数
              arg[0] = tf->tf_regs.reg_edx;
              arg[1] = tf->tf_regs.reg_ecx;
              arg[2] = tf->tf_regs.reg_ebx;
              arg[3] = tf->tf_regs.reg_edi;
              arg[4] = tf->tf_regs.reg_esi;
              // 结果存到寄存器a对应的堆栈中，系统调用结束时堆栈结果恢复到寄存器，返回结果到寄存器a
              tf->tf_regs.reg_eax = syscalls[num](arg);
              return ;
          }
      }
      print_trapframe(tf);
      panic("undefined syscall %d, pid = %d, name = %s.\n",
              num, current->pid, current->name);
  }
 ```

 2. 以getpid为例，分析ucore的系统调用中返回结果的传递代码。
 > syscall中sys_getpid返回pid给
 > 结果存到堆栈中对应寄存器a的位置
 > 返回应用程序的时候，堆栈结果恢复到寄存器，结果存到寄存器a中

 3. 以ucore lab8的answer为例，分析ucore 应用的系统调用编写和含义。

  ```c
      [SYS_exit]          //退出进程
      [SYS_fork]          //复制创建子进程
      [SYS_wait]          //等待进程结束
      [SYS_exec]          //加载其他可执行程序
      [SYS_yield]         //让出CPU时间
      [SYS_kill]          //删除进程
      [SYS_getpid]        //获得进程号
      [SYS_putc]          //输出一个字节
      [SYS_pgdir]         //返回页目录起始地址
      [SYS_gettime]       //获得时间
      [SYS_lab6_set_priority]  //设置优先级
      [SYS_sleep]         //睡眠
      [SYS_open]          //打开文件
      [SYS_close]         //关闭文件
      [SYS_read]          //读输入
      [SYS_write]         //写输出
      [SYS_seek]          //查找
      [SYS_fstat]         //查询文件信息
      [SYS_fsync]         //将缓存协会磁盘
      [SYS_getcwd]        //获得当前工作目录
      [SYS_getdirentry]   //获得文件描述符对应的目录信息
      [SYS_dup]           //复制文件描述符
  ```

 4. 以ucore lab8的answer为例，尝试修改并运行ucore OS kernel代码，使其具有类似Linux应用工具`strace`的功能，即能够显示出应用程序发出的系统调用，从而可以分析ucore应用的系统调用执行过程。
 > 在syscall()函数中加一个输出
 
## 3.6 请分析函数调用和系统调用的区别
 1. 请从代码编写和执行过程来说明。
 2. 说明`int`、`iret`、`call`和`ret`的指令准确功能
 

## v9-cpu相关题目
---

### 提前准备
```
cd YOUR v9-cpu DIR
git pull 
cd YOUR os_course_spoc_exercise DIR
git pull 
```

### v9-cpu系统调用实现
  1. v9-cpu中os4.c的系统调用中参数传递代码分析。
  2. v9-cpu中os4.c的系统调用中返回结果的传递代码分析。
  3. 理解v9-cpu中os4.c的系统调用编写和含义。

