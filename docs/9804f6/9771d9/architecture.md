# 架构设计 - 设计和实现游戏UI界面

## 架构模式
MVC + 组件化架构

## 技术栈

- **language**: JavaScript ES6+
- **framework**: 原生HTML5 Canvas
- **database**: LocalStorage（本地存储）
- **others**: CSS3, Flexbox/Grid布局, Canvas 2D API, RequestAnimationFrame

## 模块设计

### UIManager
职责: 统一管理所有UI组件的渲染、更新和布局
- init()
- render()
- updateScore()
- updateLevel()
- updateLines()
- updateNextPiece()
- resize()

### GameBoard
职责: 游戏主区域渲染，包括10x20网格、当前方块、已放置方块
- render(gameState)
- drawGrid()
- drawActivePiece()
- drawPlacedPieces()
- highlightFullLines()

### ScorePanel
职责: 分数、等级、行数等游戏统计信息显示
- updateScore(score)
- updateLevel(level)
- updateLines(lines)
- render()

### NextPiecePreview
职责: 下个方块预览区域的渲染
- updateNextPiece(pieceType)
- render()
- drawPreviewPiece()

### ResponsiveLayout
职责: 处理不同屏幕尺寸的响应式布局适配
- calculateLayout()
- adjustCanvasSize()
- updateUIScale()
- handleResize()

### ThemeManager
职责: 管理游戏主题、颜色方案和视觉效果
- setTheme(themeName)
- getColors()
- applyEffects()
- loadTheme()

## 数据流
GameState -> UIManager -> 各UI组件 -> Canvas渲染。游戏状态变化时，UIManager接收更新请求，分发给对应的UI组件进行重绘。ResponsiveLayout监听窗口变化事件，动态调整布局参数。所有渲染操作最终通过Canvas 2D API输出到屏幕。

## 风险点
- 不同设备屏幕尺寸适配复杂度较高
- Canvas渲染性能在低端设备上可能不足
- UI组件间的状态同步可能出现延迟
- 字体和图形在高DPI屏幕上的清晰度问题

## 关键决策
- 采用Canvas而非DOM元素实现UI，确保60FPS性能
- 使用组件化设计模式，便于维护和扩展
- 实现响应式布局系统，支持移动端和桌面端
- 预留主题系统接口，支持后续视觉定制
- 使用requestAnimationFrame确保流畅的UI更新
- 采用相对单位和比例计算，适配不同分辨率
