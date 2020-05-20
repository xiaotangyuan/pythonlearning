"""
learning logging module

通过使用最简化的功能为线索，来阅读源码
通过代码追踪，弄清楚代码的执行调用路线
"""

import logging
logging.warning('test')
"""
因为没有配置生成自定义的logger, 此处调用了全局变量root这个logger来输出信息
"""


