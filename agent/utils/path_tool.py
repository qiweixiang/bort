import os


def get_project_agent_root():
    """
    获取项目根路径
    :return:
    """
    # 获取当前文件所在的绝对路径
    current_file_path = os.path.abspath(__file__)
    # 获取当前文件所在的目录的位置  其实就是向上进了一层
    dir_path = os.path.dirname(current_file_path)
    # 再向上进一层 就是项目根路径  进几层取决于该文件的位置
    return os.path.dirname(dir_path)


def get_abs_path(relative_path :str) -> str :
    """
    根据相对路径获取绝对路径
    :param relative_path:
    :return:
    """
    # 连接两个路径
    return os.path.join(get_project_agent_root(), relative_path)


if __name__ == '__main__':
    # print(get_project_root())
    print(get_abs_path("config/aa.txt"))