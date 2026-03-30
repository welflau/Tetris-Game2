# 架构设计 - 用户界面开发

## 架构模式
MVC + 组件化架构

## 技术栈

- **language**: JavaScript ES6+
- **framework**: 原生JavaScript + HTML5 Canvas
- **database**: LocalStorage
- **others**: CSS3, Web Audio API, requestAnimationFrame

## 模块设计

### UIManager
职责: 统一管理所有UI组件的创建、更新和销毁
- init()
- render()
- updateGameState(state)
- showPauseMenu()
- hidePauseMenu()

### GameCanvas
职责: 管理主游戏区域Canvas渲染，包括游戏网格、方块绘制
- drawGrid()
- drawTetromino(tetromino)
- drawGhostPiece(tetromino)
- clear()
- resize()

### InfoPanel
职责: 显示游戏信息面板，包括分数、等级、行数等统计信息
- updateScore(score)
- updateLevel(level)
- updateLines(lines)
- updateTime(time)

### PreviewPanel
职责: 显示下一个方块预览和保留方块区域
- showNextPiece(tetromino)
- showHoldPiece(tetromino)
- clearPreview()

### ControlPanel
职责: 游戏控制按钮区域，包括暂停、重新开始等功能
- showPauseButton()
- showResumeButton()
- showRestartButton()
- bindEvents()

### ResponsiveLayout
职责: 处理响应式布局适配，确保在不同屏幕尺寸下的良好显示
- calculateLayout()
- adjustCanvasSize()
- repositionElements()
- handleResize()

### ThemeManager
职责: 管理游戏主题和视觉样式，支持主题切换
- loadTheme(themeName)
- applyColors()
- updateBlockStyles()
- saveThemePreference()

## 数据流
GameController触发状态更新 -> UIManager接收状态变化 -> 分发到各个UI组件 -> 组件更新各自显示内容 -> Canvas重绘游戏画面 -> 用户交互事件通过EventHandler回传给GameController

## 风险点
- 不同浏览器Canvas渲染性能差异
- 移动端触摸操作适配复杂性
- 高分辨率屏幕下Canvas模糊问题
- 响应式布局在极端屏幕比例下的显示问题

## 关键决策
- 采用CSS Grid布局实现响应式设计，确保各组件合理排列
- 使用Canvas 2D Context进行游戏区域渲染，提供最佳性能
- 实现组件化UI架构，便于维护和扩展
- 采用CSS变量管理主题色彩，支持动态主题切换
- 使用Flexbox处理信息面板内部布局，确保内容对齐
- 实现Canvas高DPI适配，解决高分辨率屏幕模糊问题
