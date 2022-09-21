from functional import seq


class Strs:
    """ 提供字符串的增强操作 """

    @staticmethod
    def multiline(s: str) -> str:
        """
        修复Python多行字符串的计入换行和左空格的问题

        :param s: 原字符串
        :return: 结果字符串
        """

        return seq(s.split("\n")[1: -1]) \
            .map(str.lstrip) \
            .reduce(lambda t1, t2: t1 + '\n' + t2)
