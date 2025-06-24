from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
import time


class SleepTool(Tool):
    """一个让工作流暂停指定时间的工具"""
    
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        """
        执行睡眠操作
        
        Args:
            tool_parameters: 包含时间参数的字典
            
        Yields:
            ToolInvokeMessage: 操作结果消息
        """
        try:
            # 获取参数，使用get()避免KeyError，并提供默认值0
            year = tool_parameters.get("year", 0)
            month = tool_parameters.get("month", 0)
            day = tool_parameters.get("day", 0)
            hour = tool_parameters.get("hour", 0)
            minute = tool_parameters.get("minute", 0)
            second = tool_parameters.get("second", 0)  
            
            year = float(year) if year is not None else 0
            month = float(month) if month is not None else 0
            day = float(day) if day is not None else 0
            hour = float(hour) if hour is not None else 0
            minute = float(minute) if minute is not None else 0
            second = float(second) if second is not None else 0
            
            # 参数验证：确保非负数
            if any(param < 0 for param in [year, month, day, hour, minute, second]):
                yield self.create_text_message("Error: Time parameters cannot be negative.")
                return
            
            # 计算总秒数（每月平均30.44天，每年365.25天以考虑闰年）
            total_days = day + month * 30.44 + year * 365.25
            total_seconds = int(total_days * 24 * 60 * 60)  # 天转换为秒
            total_seconds += hour * 60 * 60  # 小时转换为秒
            total_seconds += minute * 60  # 分钟转换为秒
            total_seconds += second  # 加上秒
            
            # 执行睡眠
            time.sleep(total_seconds)
            
            # 返回结果
            yield self.create_text_message(f"Sleep completed successfully for {total_seconds} seconds.")
            
        except Exception as e:
            yield self.create_text_message(f"Error during sleep operation: {str(e)}")