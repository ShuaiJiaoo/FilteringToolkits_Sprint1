# coding:utf-8

from pm4py.objects.log.importer.csv import factory as csv_importer  # 导入csv 文件，结果为 event_stream
from pm4py.objects.log.importer.xes import factory as importer      # 导入xes 文件，结果为 log
from pm4py.objects.conversion.log import factory as conversion_factory
from pm4py.algo.discovery.alpha import factory as alpha_miner
from pm4py.visualization.petrinet import factory as visualizer
from pm4py.util import constants
import global_util
import os


# 导入事件日志
def import_xes_data(filename):
    if not os.path.abspath(filename):
        # 修改日志文件路径
        file_path = global_util.get_full_path_input_file(filename)
    else:
        file_path = filename
        filename = os.path.basename(filename)

    # 导入日志文件名
    parameters = {"timestamp_sort": True}
    log = importer.apply(file_path, variant="nonstandard", parameters=parameters)

    # 矿工应用日志文件
    net, initial_marking, final_marking = alpha_miner.apply(log)

    # 可视化界面应用分析结果
    gviz = visualizer.apply(net, initial_marking, final_marking)

    # 生成输出文件名
    file, _ = os.path.splitext(filename)
    output_full_name = "output_" + file + ".png"
    # 生成输出文件全路径
    output_file = global_util.get_full_path_output_file(output_full_name)

    # 保存文件
    visualizer.save(gviz, output_file)
    # 返回输出文件名
    return output_full_name


# 导入csv 文件
def import_csv_file(filename):
    filename = os.path.basename(filename)
    # 修改日志文件路径
    file_path = global_util.get_full_path_input_file(filename)

    # 将文件按 csv 文件格式导入，得到事件流结构
    event_stream = csv_importer.import_event_stream(file_path)
    # dataframe = csv_import_adapter.import_dataframe_from_path(file_path, sep=",")

    # 将事件流转换成 xes 结构
    log = conversion_factory.apply(event_stream, parameters={constants.PARAMETER_CONSTANT_TIMESTAMP_KEY: "日期和时间"})

    # 矿工应用日志文件，这里简单的应用阿尔法矿工
    net, initial_marking, final_marking = alpha_miner.apply(log)

    # 可视化界面应用分析结果
    gviz = visualizer.apply(net, initial_marking, final_marking)

    # 显示结果
    visualizer.view(gviz)


def test_import_xes_data(filename):
    filename = os.path.basename(filename)

    # 修改日志文件路径
    file_path = global_util.get_full_path_test_file(filename)

    # 导入日志文件名
    log = importer.apply(file_path)
    for case_index, case in enumerate(log):
        print("\n case index: %d  case id: %s" % (case_index, case.attributes["concept:name"]))
        for event_index, event in enumerate(case):
            print("event index: %d  event activity: %s" % (event_index, event["concept:name"]))

    # 设置过滤器重新导入
    parameters = {"timestamp_sort": True}
    log = importer.apply(file_path, variant="nonstandard", parameters=parameters)
    for case_index, case in enumerate(log):
        print("\n case index: %d  case id: %s" % (case_index, case.attributes["concept:name"]))
        for event_index, event in enumerate(case):
            print("event index: %d  event activity: %s" % (event_index, event["concept:name"]))


if __name__ == "__main__":
    # test_import_xes_data("running.xes")
    import_xes_data("running.xes")
