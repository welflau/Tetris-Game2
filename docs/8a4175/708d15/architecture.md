# 架构设计 - 实现游戏状态管理和UI界面

## 架构模式
MVC + 状态机模式

## 技术栈

- **language**: JavaScript (ES6+)
- **framework**: 原生JavaScript + Canvas API
- **database**: LocalStorage (本地存储)
- **others**: HTML5 Canvas, CSS3, Web APIs

## 模块设计

### GameStateManager
职责: 管理游戏状态（开始、暂停、结束、游戏中）的切换和状态持久化
- setState(state)
- getState()
- isPlaying()
- isPaused()
- isGameOver()

### ScoreManager
职责: 处理得分计算、等级提升、最高分记录等功能
- addScore(lines)
- getScore()
- getLevel()
- getHighScore()
- saveHighScore()

### UIRenderer
职责: 渲染游戏界面元素，包括得分、等级、下一个方块预览、游戏状态提示
- renderScore()
- renderLevel()
- renderNextPiece()
- renderGameState()
- renderStats()

### PreviewManager
职责: 管理下一个方块的生成和预览显示
- generateNext()
- getNext()
- renderPreview()
- swapCurrent()

### MenuSystem
职责: 处理游戏菜单、暂停界面、游戏结束界面的显示和交互
- showStartMenu()
- showPauseMenu()
- showGameOverMenu()
- hideMenus()

### InputHandler
职责: 扩展输入处理，支持菜单导航和游戏状态切换
- handleMenuInput()
- handleGameInput()
- bindStateControls()

### AudioManager
职责: 管理游戏音效和背景音乐
- playSound(type)
- playMusic()
- stopMusic()
- setVolume(level)

### StorageManager
职责: 处理游戏数据的本地存储和读取
- saveGameData()
- loadGameData()
- clearData()
- saveSettings()

## 数据流
用户输入 -> InputHandler -> GameStateManager -> 根据状态分发到对应管理器 -> ScoreManager/PreviewManager更新数据 -> UIRenderer渲染界面 -> StorageManager持久化数据。游戏状态变化触发MenuSystem显示相应界面，AudioManager根据游戏事件播放音效。

## 风险点
- 状态切换逻辑复杂，可能出现状态不一致
- UI渲染性能问题，特别是频繁更新的得分显示
- 本地存储数据格式兼容性问题
- 音频播放在不同浏览器的兼容性差异
- 响应式设计在不同设备上的适配问题

## 关键决策
- 采用状态机模式管理游戏状态，确保状态切换的可控性
- 使用观察者模式实现UI更新，减少模块间耦合
- 将UI渲染与游戏逻辑分离，提高代码可维护性
- 使用LocalStorage存储游戏数据，无需服务器支持
- 采用Canvas双缓冲技术优化渲染性能
- 实现音频预加载机制，提升用户体验
- 使用CSS媒体查询实现响应式布局
