# 架构设计 - 用户界面设计与实现

## 架构模式
MVC模式的UI层设计

## 技术栈

- **language**: JavaScript ES6+
- **framework**: 原生HTML5/CSS3/Canvas

## 模块设计

### UIManager
职责: 统一管理游戏界面布局和组件
- init()
- updateScore()
- updateLevel()
- updateLines()
- showGameOver()
- showPause()

### GameBoard
职责: 游戏主区域Canvas渲染和交互
- render()
- drawGrid()
- drawTetromino()
- clear()

### InfoPanel
职责: 信息显示区域（分数、等级、行数）
- updateDisplay()
- formatScore()
- animateScoreChange()

### PreviewPanel
职责: 下一个方块预览区域
- showNext()
- clearPreview()
- drawPreviewTetromino()

### ControlPanel
职责: 游戏控制按钮（暂停、重新开始等）
- bindEvents()
- togglePause()
- restart()

### ResponsiveLayout
职责: 响应式布局适配不同屏幕尺寸
- adjustLayout()
- handleResize()
- setMobileMode()

## 数据流
UIManager作为主控制器，协调各个面板组件。GameBoard接收游戏状态数据进行Canvas渲染，InfoPanel监听分数变化事件更新显示，PreviewPanel接收下一个方块数据，ControlPanel处理用户交互并触发游戏状态变化，ResponsiveLayout监听窗口变化调整布局

## 关键决策
- 基于现有CSS.js模块扩展，保持原有架构风格
- 使用CSS Grid和Flexbox实现响应式布局
- Canvas游戏区域采用固定宽高比，通过CSS缩放适配
- 信息面板使用数字动画效果提升用户体验
- 预览区域使用小型Canvas独立渲染
- 移动端适配采用触摸手势控制
- 使用CSS变量统一管理主题色彩
