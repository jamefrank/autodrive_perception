# -*- encoding: utf-8 -*-
#@File    :   global_config.py
#@Time    :   2024/04/25 00:46:31
#@Author  :   frank 
#@Email:
#@Description: 解析 config 文件

from argparse import ArgumentParser
from pydantic import BaseModel as PydanticBaseModel


class BaseModel(PydanticBaseModel):
    class Config:
        arbitrary_types_allowed = True

class GlobalConfigParam(BaseModel):
    pass

# 解析config变量等
def global_config_parse()->GlobalConfigParam:
    parser = ArgumentParser(description="command line parse")
    
    # parser.add_argument("filename", type=str, help="要处理的文件名")  
    parser.add_argument('-c', '--config', type=str, help='global config path')
    parser.add_argument('-p', '--pretrain', type=str, help='pretrain model dir')
    parser.add_argument('-s', '--save', type=str, help='output dir')
    parser.add_argument('-r', '--resume', type=str, help='train model snapshot dir')
    parser.add_argument('-i', '--image', type=str, help='image dir')
    parser.add_argument('-j', '--json', type=str, help='json path')
    parser.add_argument('-f', '--txt', type=str, help='txt path')
    parser.add_argument('-m', '--mode', type=str, help='phase mode')
    
    parser.add_argument('-g', '--gpus', type=str, help='gpus')
    parser.add_argument('-t', '--tasks', type=str, help='activate tasks')
    parser.add_argument('--precision', type=int, default=32, choices=[8, 16, 32],help='numerical precision')
    parser.add_argument('--seed', type=int,help='fixed random seed')
    parser.add_argument('--log_level', type=str, default='INFO',help='logging level')
    
    parser.add_argument('--freeze_backbone', action='store_true',help='freeze backbone network')
    
    args = parser.parse_args()
    
    if not args.mode:
        parser.error("mode need be set")
        
    #
    global_config = GlobalConfigParam()
    
    
    return global_config
    


if __name__ == '__main__':
    global_config = global_config_parse()
