# -*- encoding: utf-8 -*-
#@File    :   argparser-note.py
#@Time    :   2024/04/24 23:01:31
#@Author  :   frank 
#@Email:
#@Description:

import argparse  
  
def main():  
    # 创建 ArgumentParser 对象  
    parser = argparse.ArgumentParser(description="一个简单的命令行工具示例")  
  
    # 添加位置参数  
    parser.add_argument("filename", type=str, help="要处理的文件名")  
  
    # 添加可选参数  
    parser.add_argument("-v", "--verbose", action="store_true", help="是否输出详细信息")  
  
    # 解析命令行参数  
    args = parser.parse_args()  
  
    # 根据参数执行操作  
    print(f"处理文件: {args.filename}")  
    if args.verbose:  
        print("详细信息模式已开启")  
    else:  
        print("详细信息模式已关闭")  
  
if __name__ == "__main__":  
    main()