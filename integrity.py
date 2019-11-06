from hashlib import md5, sha1, sha256
import sys

path_to_file = sys.argv[1]
path_to_dir = sys.argv[2]

with open(path_to_file) as f:
    for line in f:
        line = line.rstrip()
        file_name, algorithm, etalon_hash = line.split()

        if algorithm == "md5":
            try:
                real_hash = md5(open(path_to_dir + file_name, "rb").read().rstrip()).hexdigest()
                if etalon_hash == real_hash:
                    print(file_name, "OK")
                else:
                    print(file_name, "FAIL")
            except FileNotFoundError:
                print(file_name, "NOT FOUND")
        elif algorithm == "sha1":
            try:
                real_hash = sha1(open(path_to_dir + file_name, "rb").read().rstrip()).hexdigest()
                if etalon_hash == real_hash:
                    print(file_name, "OK")
                else:
                    print(file_name, "FAIL")
            except FileNotFoundError:
                print(file_name, "NOT FOUND")
        elif algorithm == "sha256":
            try:
                real_hash = sha256(open(path_to_dir + file_name, "rb").read().rstrip()).hexdigest()
                if etalon_hash == real_hash:
                    print(file_name, "OK")
                else:
                    print(file_name, "FAIL")
            except FileNotFoundError:
                print(file_name, "NOT FOUND")