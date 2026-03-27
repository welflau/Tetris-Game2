# 架构设计 - 信息面板界面设计

## 架构模式
组件化UI架构

## 技术栈

- **language**: JavaScript/TypeScript
- **framework**: HTML5 Canvas + CSS3
- **database**: LocalStorage
- **others**: CSS Grid/Flexbox, Web Fonts, CSS Animations, Responsive Design

## 模块设计

### InfoPanelManager
职责: 统一管理所有信息面板的显示、更新和布局
- updateScore(score)
- updateLevel(level)
- updateLines(lines)
- updateNextPiece(piece)
- render()

### ScoreDisplay
职责: 显示当前分数、最高分数和分数变化动画
- setScore(score)
- setHighScore(score)
- animateScoreIncrease(increment)
- render()

### LevelDisplay
职责: 显示当前等级、进度条和等级提升效果
- setLevel(level)
- setProgress(percentage)
- animateLevelUp()
- render()

### NextPiecePreview
职责: 预览下一个方块的形状和颜色
- setNextPiece(pieceType)
- renderPreview()
- animateTransition()

### StatisticsPanel
职责: 显示游戏统计信息如消除行数、游戏时间等
- updateLines(lines)
- updateTime(time)
- updateStatistics(stats)
- render()

### ThemeManager
职责: 管理信息面板的主题样式和响应式布局
- setTheme(theme)
- applyResponsiveLayout()
- updateColors(colorScheme)

## 数据流
游戏引擎 -> InfoPanelManager -> 各子组件 -> DOM渲染。游戏状态变化时，引擎通知InfoPanelManager，由其分发更新到对应的显示组件，各组件独立处理自己的渲染逻辑和动画效果

## 风险点
- 不同屏幕尺寸下的布局适配问题
- 动画效果可能影响游戏性能
- 字体和图标在不同设备上的显示一致性
- 信息更新频率过高导致界面闪烁

## 关键决策
- 采用CSS Grid布局确保信息面板的灵活排列
- 使用CSS3动画而非JavaScript动画提升性能
- 实现响应式设计支持移动端和桌面端
- 采用组件化设计便于主题切换和样式定制
- 使用防抖机制控制信息更新频率避免界面抖动
