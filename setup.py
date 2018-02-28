# from os.path import dirname, join
from setuptools import setup, find_packages

root_pack = 'moear.spider.zhihudaily'


setup(
    name='moear-spider-zhihudaily',
    url='https://github.com/littlemo/moear-spider-zhihudaily',
    author='moear developers',
    author_email='moore@moorehy.com',
    maintainer='littlemo',
    maintainer_email='moore@moorehy.com',
    version='1.0.0',
    description='MoEar扩展爬虫功能插件的通用组件',
    long_description='test',
    keywords='moear scrapy',
    packages=find_packages(exclude=('docs', 'tests', 'tests.*')),
    include_package_data=True,
    zip_safe=False,
    license='GPLv3',
    provides=[
        'moear.spider',
    ],
    install_requires=[
        'Scrapy~=1.5.0',
        'beautifulsoup4~=4.6.0',
        'moear-spider-common~=1.0.0',
    ],
    entry_points={
        'moear.spider': [
            'zhihudaily = {}:ZhihuDaily'.format(root_pack),
        ],
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Environment :: MacOS X',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Natural Language :: Chinese (Simplified)',
        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Terminals',
        'Topic :: Utilities',
    ],
)