# lec5 SPOC思考题

## 提前准备

- 完成lec５的视频学习和提交对应的在线练习
- git pull ucore_os_lab, v9_cpu, os_course_spoc_exercises 　in github repos。这样可以在本机上完成课堂练习。
- 理解连续内存动态分配算法的实现（主要自学和网上查找）

NOTICE
- 有"w3l1"标记的题是助教要提交到学堂在线上的。
- 有"w3l1"和"spoc"标记的题是要求拿清华学分的同学要在实体课上完成，并按时提交到学生对应的git repo上。
- 有"hard"标记的题有一定难度，鼓励实现。
- 有"easy"标记的题很容易实现，鼓励实现。
- 有"midd"标记的题是一般水平，鼓励实现。


## 个人思考题
---

请简要分析最优匹配，最差匹配，最先匹配，buddy systemm分配算法的优势和劣势，并尝试提出一种更有效的连续内存分配算法 (w3l1)
```
  + 采分点：说明四种算法的优点和缺点
  - 答案没有涉及如下3点；（0分）
  - 正确描述了二种分配算法的优势和劣势（1分）
  - 正确描述了四种分配算法的优势和劣势（2分）
  - 除上述两点外，进一步描述了一种更有效的分配算法（3分）
 ```
- [x]  

>  

## 小组思考题

请参考xv6（umalloc.c），ucore lab2代码，选择四种（0:最优匹配，1:最差匹配，2:最先匹配，3:buddy systemm）分配算法中的一种或多种，在Linux应用程序/库层面，用C、C++或python来实现malloc/free，给出你的设计思路，并给出可以在Linux上运行的malloc/free实现和测试用例。 (spoc)

- [基于malloc与free函数的实现代码及分析](http://www.jb51.net/article/36391.htm)

```python
# mm manager, first_fit

occupied_space = dict()
free_space = dict()


def _mm_init():
    global free_space
    free_space = dict({0: 1024})
    global occupied_space
    occupied_space = dict()


def _free(start):
    if start in occupied_space:
        len = occupied_space[start]
        occupied_space.pop(start, None)
        free_space[start] = len
        s = start
        # merge
        for i in range(0, 1024):
            if i in free_space and free_space[i] + i == start:
                free_space[i] = free_space[i] + len
                free_space.pop(start, None)
                s = i
                break
        if (s + free_space[s]) in free_space:
            free_space[s] = free_space[s] + free_space[s + free_space[s]]
            free_space.pop(s + free_space[s], None)
        return len
    return -1


def _malloc(size):
    for i in range(0, 1024):
        if i in free_space and free_space[i] >= size:
            free_space[i + size] = free_space[i] - size
            free_space.pop(i, None)
            occupied_space[i] = size
            return i
    return -1


def main():
    _mm_init()
    start0 = _malloc(10)
    print(start0)
    start1 = _malloc(20)
    print(start1)
    start2 = _malloc(30)
    print(start2)
    print(_free(start1))
    print(_free(start0))
    start3 = _malloc(25)
    print(start3)

if __name__ == "__main__":
    main()
```

```
如何表示空闲块？ 如何表示空闲块列表？ 
[(start0, size0),(start1,size1)...]
在一次malloc后，如果根据某种顺序查找符合malloc要求的空闲块？如何把一个空闲块改变成另外一个空闲块，或消除这个空闲块？如何更新空闲块列表？
在一次free后，如何把已使用块转变成空闲块，并按照某种顺序（起始地址，块大小）插入到空闲块列表中？考虑需要合并相邻空闲块，形成更大的空闲块？
如果考虑地址对齐（比如按照4字节对齐），应该如何设计？
如果考虑空闲/使用块列表组织中有部分元数据，比如表示链接信息，如何给malloc返回有效可用的空闲块地址而不破坏
元数据信息？
伙伴分配器的一个极简实现
http://coolshell.cn/tag/buddy
```

--- 

## 扩展思考题

阅读[slab分配算法](http://en.wikipedia.org/wiki/Slab_allocation)，尝试在应用程序中实现slab分配算法，给出设计方案和测试用例。

## “连续内存分配”与视频相关的课堂练习

### 5.1 计算机体系结构和内存层次
MMU的工作机理？

- [x]  

>  http://en.wikipedia.org/wiki/Memory_management_unit

L1和L2高速缓存有什么区别？

- [x]  

>  http://superuser.com/questions/196143/where-exactly-l1-l2-and-l3-caches-located-in-computer
>  Where exactly L1, L2 and L3 Caches located in computer?

>  http://en.wikipedia.org/wiki/CPU_cache
>  CPU cache

### 5.2 地址空间和地址生成
编译、链接和加载的过程了解？

- [x]  

>  

动态链接如何使用？

- [x]  

>  


### 5.3 连续内存分配
什么是内碎片、外碎片？

- [x]  

>  

为什么最先匹配会越用越慢？

- [x]  

>  

为什么最差匹配会的外碎片少？

- [x]  

>  

在几种算法中分区释放后的合并处理如何做？

- [x]  

>  

### 5.4 碎片整理
一个处于等待状态的进程被对换到外存（对换等待状态）后，等待事件出现了。操作系统需要如何响应？

- [x]  

>  

### 5.5 伙伴系统
伙伴系统的空闲块如何组织？

- [x]  

>  

伙伴系统的内存分配流程？

- [x]  

>  

伙伴系统的内存回收流程？

- [x]  

>  

struct list_entry是如何把数据元素组织成链表的？

- [x]  

>  



## v9-cpu相关

[challenge]在v9-cpu上完成基于method-0/1/2/buddy system（选一个方法）with first/best/worst-fit(选一个fit)用户态动态内存分配函数malloc/free，要求在内核态实现sbrk系统调用以支持用户态动态内存分配方法。基于os4.c实现，可参考v9-cpu git repo的testing分支中的os.c和mem.h

- [x]  

> 

[challenge]在v9-cpu上完成基GC算法，要求在内核态实现sbrk系统调用以支持用户态动态内存分配方法。基于os4.c实现，可参考v9-cpu git repo的testing分支中的os.c和mem.h

- [x]  

>

## 其它
- 静态分配内存与动态分配内存的区别是啥？
- 在隐式链表结构中，如何实现向前的合并操作？
- 如何判断一个函数是库函数还是一个系统调用？
- 为何要在OS内部和用户态中实现两层动态内存分配？
- 为何在OS内部没有采用GC分配方式？
