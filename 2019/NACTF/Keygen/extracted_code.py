# undefined8 check_letters_numbers(char *param_1)
# {
#   ulonglong uVar1;
#   uint uVar2;
#   bool bVar3;
#   char *KEY;
#   uint local_c;
#   int local_8;
  
#   local_c = 0;
#   local_8 = 0;
#   KEY = param_1;
#   while (KEY < param_1 + 8) {
#     uVar1 = (ulonglong)local_c;
#     local_c = (uint)(uVar1 * 0x3e);
#     local_8 = local_8 * 0x3e + (int)(uVar1 * 0x3e >> 0x20);
#     if (('@' < *KEY) && (*KEY < '[')) {
#       uVar2 = (int)*KEY - 0x41;
#       bVar3 = CARRY4(local_c,uVar2);
#       local_c = local_c + uVar2;
#       local_8 = local_8 + ((int)uVar2 >> 0x1f) + (uint)bVar3;
#     }
#     if (('`' < *KEY) && (*KEY < '{')) {
#       uVar2 = (int)*KEY - 0x47;
#       bVar3 = CARRY4(local_c,uVar2);
#       local_c = local_c + uVar2;
#       local_8 = local_8 + ((int)uVar2 >> 0x1f) + (uint)bVar3;
#     }
#     if (('/' < *KEY) && (*KEY < ':')) {
#       uVar2 = (int)*KEY + 4;
#       bVar3 = CARRY4(local_c,uVar2);
#       local_c = local_c + uVar2;
#       local_8 = local_8 + ((int)uVar2 >> 0x1f) + (uint)bVar3;
#     }
#     KEY = KEY + 1;
#   }
#   return CONCAT44(local_8,local_c);
# }

import sys

def usage():
    print("Usage: script.py <INPUT_STR>")
    exit()

if __name__ == "__main__": 

    if len(sys.argv) != 2:
        usage()

    flag = sys.argv[1]

    if len(flag) != 8:
        print("Incorrect flag len!")
        exit()

    count = 0
    for s in flag:
        
        count = count * 0x3e

        if '@' < s and s < '[':
            count += ord(s) - 0x41

        if '`' < s and s < '{':
            count += ord(s) - 0x47

        if '/' < s and s < ':':
            count += ord(s) + 4

    print(hex(count))