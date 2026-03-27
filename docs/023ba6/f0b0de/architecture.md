# 架构设计 - 实现基础方块绘制功能

## 架构模式
MVC + 组件化架构

## 技术栈

- **language**: JavaScript/TypeScript
- **framework**: 原生Canvas API
- **database**: 内存存储（二维数组）
- **others**: HTML5 Canvas, CSS3, ES6+ 模块系统

## 模块设计

### Renderer模块
职责: 负责Canvas渲染管理，包括方块绘制、网格绘制、颜色管理
- drawBlock(x, y, color)
- drawGrid()
- clearCanvas()
- setBlockSize(size)

### Block模块
职责: 定义方块的基础属性和绘制逻辑，管理方块状态
- Block(x, y, color, type)
- render()
- getPosition()
- setColor(color)

### ColorManager模块
职责: 管理游戏中所有颜色配置，提供颜色映射和主题支持
- getColor(type)
- setTheme(theme)
- getGridColor()
- getBorderColor()

### CoordinateSystem模块
职责: 处理逻辑坐标与Canvas像素坐标的转换
- logicToPixel(x, y)
- pixelToLogic(x, y)
- getBlockSize()
- getBoardOffset()

## 数据流
Game类调用Board类获取网格状态 → Board类通过Renderer模块绘制网格 → Renderer调用Block模块绘制单个方块 → Block模块使用ColorManager获取颜色 → CoordinateSystem提供坐标转换支持 → 最终在Canvas上渲染完整画面

## 风险点
- Canvas性能问题，频繁重绘可能导致卡顿
- 不同浏览器Canvas渲染差异
- 坐标系统计算错误导致方块位置偏移
- 颜色管理复杂度增加维护成本

## 关键决策
- 使用Canvas 2D API而非WebGL，优先考虑兼容性和开发效率
- 采用逻辑坐标系统，便于游戏逻辑与渲染分离
- 实现颜色配置化管理，支持后续主题扩展
- 使用双缓冲机制减少闪烁，提升渲染性能
- 方块绘制采用填充+描边模式，增强视觉效果
