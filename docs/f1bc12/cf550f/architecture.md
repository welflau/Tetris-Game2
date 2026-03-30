# 架构设计 - Canvas渲染系统开发

## 架构模式
模块化Canvas渲染架构

## 技术栈

- **language**: JavaScript ES6+
- **framework**: 原生Canvas API + 现有CSS模块

## 模块设计

### CanvasRenderer
职责: Canvas渲染引擎核心，管理画布初始化、坐标系统、基础绘制方法
- init(canvasId, width, height)
- clear()
- drawRect(x, y, width, height, color)
- drawText(text, x, y, style)
- setTransform(matrix)

### GameAreaRenderer
职责: 游戏区域渲染器，绘制10x20网格、边界、背景
- drawGrid()
- drawBorder()
- drawBackground()
- highlightCell(x, y, color)

### TetrominoRenderer
职责: 方块渲染器，处理7种Tetromino的绘制、阴影效果
- drawTetromino(tetromino, x, y)
- drawGhostPiece(tetromino, x, y)
- drawPreview(tetromino, previewArea)
- animateLineClear(lines)

### UIRenderer
职责: 界面元素渲染器，显示分数、等级、下一个方块预览
- drawScore(score)
- drawLevel(level)
- drawNextPiece(tetromino)
- drawGameStatus(status)

### RenderManager
职责: 渲染管理器，协调各渲染器，优化渲染性能
- render(gameState)
- startRenderLoop()
- stopRenderLoop()
- setFPS(fps)

## 数据流
RenderManager接收游戏状态数据 -> 分发给各专门渲染器 -> CanvasRenderer提供底层绘制API -> 各渲染器调用Canvas API绘制对应元素 -> 通过requestAnimationFrame实现流畅动画循环

## 关键决策
- 采用分层渲染架构，将Canvas渲染分解为专门的渲染器模块
- 使用requestAnimationFrame替代setInterval实现流畅动画
- 实现脏矩形优化，只重绘变化区域提升性能
- 集成现有CSS模块的样式系统，保持视觉一致性
- 预留动画接口支持后续音效和特效扩展
- 采用坐标映射系统，支持响应式Canvas缩放
