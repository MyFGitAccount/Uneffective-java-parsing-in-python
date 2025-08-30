#!/usr/bin/env python3
import pprint

pp=pprint.PrettyPrinter()
file_path:str="./Main.class"

CONSTANT_Class 			=7
CONSTANT_Fieldref 		=9
CONSTANT_Methodref 		=10
CONSTANT_InterfaceMethodref 	=11
CONSTANT_String 		=8
CONSTANT_Integer 		=3
CONSTANT_Float 			=4
CONSTANT_Long 			=5
CONSTANT_Double 		=6
CONSTANT_NameAndType 		=12
CONSTANT_Utf8 			=1
CONSTANT_MethodHandle 		=15
CONSTANT_MethodType 		=16
CONSTANT_InvokeDynamic 		=18


def parse_u4(f):
    return int.from_bytes(f.read(4),"big")

def parse_u2(f):
   return int.from_bytes(f.read(2),"big")

def parse_u1(f):
   return int.from_bytes(f.read(1),"big")

def read_file(file_path:str)->bytes:
   with open(file_path,"rb") as f:
        #magic=f.read(4)
        dir={}
        #cp_info={}
        dir["magic"]=hex(parse_u4(f)) #0xcafebabe
        dir["minor_ver"]=parse_u2(f) #0
        dir["major_ver"]=parse_u2(f) #69
        dir["constant_pool_count"]=parse_u2(f) #29
        const_pool=[]
        #print(dir)
        for cp in range(dir["constant_pool_count"]-1):
           cp_info={}
           value=parse_u1(f)
           if value==CONSTANT_Class:
              cp_info['tag']="CONSTANT_Class"
              cp_info['name_index']=parse_u2(f)
           elif value==CONSTANT_Fieldref:
              cp_info['tag']="CONSTANT_Fieldref"
              cp_info['class_index']=parse_u2(f)
              cp_info['name_and_type_index']=parse_u2(f)
           elif value==CONSTANT_Methodref:
              cp_info['tag']="CONSTANT_Methodref"
              cp_info['class_index']=parse_u2(f)
              cp_info['name_and_type_index']=parse_u2(f)
           elif value==CONSTANT_InterfaceMethodref:
              cp_info['tag']="CONSTANT_InterfaceMethodref"
              cp_info['class_index']=parse_u2(f)
              cp_info['name_and_type_index']=parse_u2(f)
           elif value==CONSTANT_String:
              cp_info['tag']="CONSTANT_String"
              cp_info['string_index']=parse_u2(f)
           elif value==CONSTANT_Integer:
              cp_info['tag']="CONSTANT_Integer"
              cp_info['bytes']=parse_u4(f)
           elif value==CONSTANT_Float:
              cp_info['tag']="CONSTANT_Float"
              cp_info['bytes']=parse_u4(f)
           elif value==CONSTANT_Long:
              cp_info['tag']="CONSTANT_Long"
              cp_info['high_bytes']=parse_u4(f)
              cp_info['low_bytes']=parse_u4(f)
           elif value==CONSTANT_Double:
              cp_info['tag']="CONSTANT_Double"
              cp_info['high_bytes']=parse_u4(f)
              cp_info['low_bytes']=parse_u4(f)
           elif value==CONSTANT_NameAndType:
              cp_info['tag']="CONSTANT_NameAndType"
              cp_info['name_index']=parse_u2(f)
              cp_info['descriptor_index']=parse_u2(f)
           elif value==CONSTANT_Utf8:
              cp_info['tag']="CONSTANT_Utf8"
              length=parse_u2(f)
              cp_info['bytes']=f.read(length)
           elif value==CONSTANT_MethodHandle:
              cp_info['tag']="CONSTANT_MethodHandle"
           elif value==CONSTANT_MethodType:
              cp_info['tag']="CONSTANT_MethodType"
           elif value==CONSTANT_InvokeDynamic:
              cp_info['tag']="CONSTANT_InvokeDynamic"
           else:
              assert False, f"Unexpected tag"
           print(cp_info)
           #const_pool.append(cp_info)
        #dir["const_pool"]=const_pool
        dir["access_flag"]=hex(parse_u2(f))
        dir["this_class"]=hex(parse_u2(f))
        dir["super_class"]=hex(parse_u2(f))
        dir["interfaces_count"]=hex(parse_u2(f))
        pp.pprint(dir)
        return f.read()

read_file(file_path)
