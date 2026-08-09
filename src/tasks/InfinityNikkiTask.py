from qfluentwidgets import FluentIcon

from src.tasks.MyBaseTask import MyBaseTask


class InfinityNikkiTask(MyBaseTask):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "无限暖暖任务"
        self.description = "无限暖暖自动化任务模板。请在此处添加任务的具体行为描述。"
        self.icon = FluentIcon.PLAY
        self.default_config.update({
            # TODO: 在此添加任务需要的配置项示例
            "运行次数": 1,
            "启用通知": True,
        })
        self.config_description.update({
            "运行次数": "任务循环执行的次数",
            "启用通知": "任务完成时是否发送系统通知",
        })
        self.config_type.update({
            "运行次数": {"type": "int", "min": 1, "max": 999},
            "启用通知": {"type": "bool"},
        })

    def run(self):
        """
        一次性任务的主入口。在此编写自动化逻辑：
        - 使用 self.screenshot() 截图
        - 使用 self.ocr() 进行文字识别
        - 使用 self.find_one() / self.find_feature() 模板匹配
        - 使用 self.click() / self.tap() 点击
        - 使用 self.wait_until() 等待条件满足
        - 使用 self.info_set() 在 UI 中展示状态
        - 使用 self.log_info(..., notify=True) 发送通知
        """
        run_count = self.config.get("运行次数", 1)
        notify = self.config.get("启用通知", True)

        self.log_info(f"任务开始，计划运行 {run_count} 次。")
        self.info_set("当前进度", f"0 / {run_count}")

        for i in range(run_count):
            self.log_info(f"执行第 {i + 1} / {run_count} 轮...")
            self.info_set("当前进度", f"{i + 1} / {run_count}")

            # TODO: 在此处添加具体的自动化步骤
            # 示例：
            # frame = self.screenshot()
            # text = self.ocr(frame=frame, match="开始", log=True)
            # if text:
            #     self.click(text)

            self.sleep(1)  # 占位延时，实际使用请替换为具体步骤

        self.log_info("任务执行完毕。", notify=notify)
