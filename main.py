# coding:utf-8
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from frame.promWindow import ProMWidget


def set_environment():
    return


def set_background():
    return


def pre_process():
    set_environment()
    set_background()
    # get_input()
    # check_exception()
    # get_category_id()
    # get_model()
    # set_model()
    # set_parameter()
    # change_model()
    return


def main():
    # 为应用做预处理
    pre_process()
    # 创建应用
    app = QApplication(sys.argv)

    ui = ProMWidget()
    ui.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
