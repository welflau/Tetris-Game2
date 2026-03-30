# 架构设计 - 实现投影方块透明度调整

## 架构模式
MVC前端架构

## 技术栈

- **language**: JavaScript
- **framework**: HTML5 Canvas
- **database**: LocalStorage
- **others**: CSS3, Canvas 2D API, 配置管理模块

## 模块设计

### GhostRenderer
职责: 负责投影方块的渲染逻辑，包括透明度计算、样式选择和绘制
- drawGhost(piece, position, style)
- setGhostOpacity(opacity)
- setGhostStyle(styleType)

### ConfigManager
职责: 管理游戏配置参数，包括投影方块透明度、样式等可配置项
- getGhostConfig()
- updateGhostConfig(config)
- resetToDefault()

### StyleCalculator
职责: 计算投影方块在不同背景下的最佳透明度和样式
- calculateOptimalOpacity(background)
- getContrastRatio(color1, color2)

### GameRenderer
职责: 游戏主渲染器，协调各个渲染模块的工作
- render(gameState)
- updateGhostDisplay()

## 数据流
ConfigManager读取配置 -> StyleCalculator计算最佳透明度 -> GhostRenderer应用样式参数 -> GameRenderer协调渲染 -> Canvas显示结果

## 风险点
- 不同设备和浏览器的Canvas渲染差异可能影响透明度效果
- 透明度过低可能导致在某些背景下投影方块不可见
- 性能影响：频繁的透明度计算可能影响游戏帧率

## 关键决策
- 采用可配置的透明度参数，支持0.1-0.5范围内调整
- 实现双重渲染模式：填充模式和轮廓模式可切换
- 使用自适应透明度算法，根据背景色自动调整对比度
- 将配置持久化到LocalStorage，保持用户偏好设置
- 采用requestAnimationFrame优化渲染性能
