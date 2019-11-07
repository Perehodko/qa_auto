from hashlib import md5, sha1, sha256
import sys

try:
    path_to_file, path_to_dir = sys.argv[1], sys.argv[2]
except IndexError as e:
    print("Arguments: {}!".format(e))
    raise SystemExit

with open(path_to_file) as f:
    for line in f:
        line = line.rstrip()
        file_name, algorithm, etalon_hash = line.split()

        try:
            text = open(path_to_dir + file_name, "rb").read().rstrip()
            if algorithm == "md5":
                real_hash = md5(text).hexdigest()
            elif algorithm == "sha1":
                real_hash = sha1(text).hexdigest()
            elif algorithm == "sha256":
                real_hash = sha256(text).hexdigest()

            if etalon_hash == real_hash:
                print(file_name, "OK")
            else:
                print(file_name, "FAIL")

        except FileNotFoundError:
            print(file_name, "NOT FOUND")
