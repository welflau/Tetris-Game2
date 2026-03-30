# 架构设计 - 项目架构设计与基础环境搭建

## 架构模式
模块化前端架构

## 技术栈

- **language**: JavaScript ES6+
- **framework**: 原生JavaScript + HTML5 Canvas

## 模块设计

### GameEngine
职责: 游戏核心引擎，管理游戏状态、游戏循环和渲染
- init()
- start()
- pause()
- reset()
- update()
- render()

### GameBoard
职责: 游戏区域管理，处理10x20网格和方块放置
- createGrid()
- isValidPosition()
- placeTetromino()
- clearLines()

### TetrominoFactory
职责: 方块工厂，创建和管理7种Tetromino类型
- createTetromino(type)
- getRandomTetromino()
- rotateTetromino()

### InputController
职责: 输入控制器，处理键盘事件和游戏控制
- bindEvents()
- handleKeyDown()
- handleKeyUp()

### UIManager
职责: 用户界面管理，显示分数、等级、预览等信息
- updateScore()
- updateLevel()
- showPreview()
- showGameOver()

### AudioManager
职责: 音效管理，播放游戏音效和背景音乐
- playSound()
- playMusic()
- setVolume()
- mute()

### StorageManager
职责: 本地存储管理，保存游戏数据和设置
- saveGame()
- loadGame()
- saveSettings()
- getHighScores()

## 数据流
用户输入 -> InputController -> GameEngine -> GameBoard/TetrominoFactory -> UIManager -> Canvas渲染，同时AudioManager处理音效，StorageManager负责数据持久化

## 关键决策
- 基于现有index.html扩展，添加Canvas元素和游戏UI结构
- 采用模块化设计，每个模块职责单一，便于维护和测试
- 使用requestAnimationFrame实现流畅的游戏循环
- 集成现有的CSS模块，确保响应式设计
- 保持与现有API路由的兼容性，为后续功能扩展预留接口
