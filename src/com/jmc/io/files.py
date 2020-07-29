import os
import shutil
import time
import zipfile


class Files:
    """Simple file operations."""

    @staticmethod
    def find(path, content):
        """Find files which match the content."""
        if not Files.__check('path', path):
            return None

        ds, fs = list(), list()

        for dirpath, dirnames, filenames in os.walk(path):
            ds.extend([os.path.join(dirpath, dirname) for dirname in dirnames if content in dirname])

            fs.extend([os.path.join(dirpath, filename) for filename in filenames if content in filename])

        return fs, ds

    @staticmethod
    def findAny(path, content):
        """Find a file which matches the content."""
        return Files.find(path, content)[0][0]

    @staticmethod
    def finds(path, content) -> str:
        """A simple find fn returns the str result."""
        s = time.time()

        fs, ds = Files.find(path, content)
        result = list()

        result.append('文件夹：')
        result.extend(ds)
        result.append(' ')

        result.append('文件：')
        result.extend(fs)
        result.append(' ')

        e = time.time()

        result.append("""共搜索到
{0}个文件夹
{1}个文件
本搜索耗时{2}秒""".format(len(ds), len(fs), int(e - s)))

        return '\n'.join(result)

    @staticmethod
    def copy(src, des):
        """Copy file or dir."""
        if not Files.__check('src or des', src, des):
            return None

        s = time.time()

        if not os.path.exists(des):
            os.makedirs(des)

        try:
            if os.path.isfile(src):
                shutil.copy(src, des)
            else:
                des += '/' + os.path.basename(src)
                shutil.copytree(src, des)
        except Exception as e:
            if not 'Operation not permitted' in str(e):
                print(e)

        e = time.time()

        return '耗时{}秒'.format(int(e - s))

    @staticmethod
    def copys(l, des):
        if not Files.__check('l', l) or len(l) < 1:
            return None

        for src in l:
            Files.copy(src, des)

    @staticmethod
    def move(src, des):
        """Move file or dir."""
        if not Files.__check('src or des', src, des):
            return None

        shutil.move(src, des)

    @staticmethod
    def rename(path, newName):
        """Rename file."""
        if not Files.__check('path or newName', path, newName):
            return None

        os.renames(path, os.path.dirname(path) + '/' + newName)

    @staticmethod
    def delete(*paths):
        """Delete file or dir."""
        if len(paths) < 1:
            return None

        s = time.time()

        for path in paths:
            if os.path.isfile(path):
                os.remove(path)
            else:
                shutil.rmtree(path)

        e = time.time()

        return '耗时{}秒'.format(int(e - s))

    @staticmethod
    def zip(src, *zip_path):
        """make archive and the format is zip."""
        if not Files.__check('src', src):
            return None

        s = time.time()

        former_cwd = os.getcwd()

        src_split = os.path.split(src)

        if src_split[0]:
            os.chdir(src_split[0])

        if len(zip_path) == 1:
            # a/b/c/x.zip -> ('a/b/c/x', '.zip')
            split = os.path.splitext(zip_path[0])
            shutil.make_archive(split[0], 'zip', base_dir=src_split[1])
        else:
            shutil.make_archive(src, 'zip', base_dir=src_split[1])

        os.chdir(former_cwd)

        e = time.time()

        return '耗时{}秒'.format(int(e - s))

    @staticmethod
    def unzip(zip_path, *des_path):
        """Unzip the zip file."""
        if not Files.__check('zip_path', zip_path):
            return None

        s = time.time()

        with zipfile.ZipFile(zip_path) as z:
            if len(des_path) == 1:
                z.extractall(des_path[0])
            else:
                z.extractall(os.path.split(zip_path)[0])

            e = time.time()

            return '耗时{}秒'.format(int(e - s))

    @staticmethod
    def read(path, mode='r') -> str:
        """Read file content to str."""
        if not Files.__check('path', path):
            return None

        with open(path, mode) as f:
            return f.read()

    @staticmethod
    def out(src, path, mode='w'):
        """Output content to a file."""
        if not Files.__check('path', path):
            return None

        parent = os.path.split(path)[0]
        if parent and not os.path.exists(parent):
            os.makedirs(parent)

        with open(path, mode) as f:
            f.write(src)

    @staticmethod
    def __check(msg, *parms):
        """Check if all the parms are correct."""
        for p in parms:
            if not bool(p):
                print('Parm error: ' + msg + ' can not be None')
                return False

        return True
