import os

with open("path.txt", "r") as f:
    path = f.read()

try:
    if not path[-1:].isdigit():
        # type
        file_type = 'lsblk --nodeps --output type '
        p_type = os.popen(file_type + path)
        p_file_type = (p_type.read().split("\n")[1])

        # size in GB
        size_command = 'df -H --output=size '
        p_size = os.popen(size_command + path)
        p_size_command = (p_size.read().split("\n")[1])
        print(path, p_file_type, p_size_command)
    else:
        # file type
        file_type = 'lsblk --nodeps --output type '
        p_type = os.popen(file_type + path)
        p_file_type = (p_type.read().split("\n")[1])

        # size in GB
        size_command = 'df -H --output=size '
        p_size = os.popen(size_command + path)
        p_size_command = (p_size.read().split("\n")[1])

        # free space in MB
        free_space = 'df -h --output=iavail '
        p_free = os.popen(free_space + path)
        p_free_space = (p_free.read().split("\n")[1])

        # type of file system
        fs_type = 'df --output=fstype '
        p_type_fs = os.popen(fs_type + path)
        p_fs_type = (p_type_fs.read().split("\n")[1])

        # mount point
        mount_point = 'df -h --output=target '
        pipe = os.popen(mount_point + path)
        p_mount_point = (pipe.read().split("\n")[1])
        print(path, p_file_type, p_size_command, p_free_space, p_fs_type, p_mount_point)

except IndexError:
    print("Device not found")
