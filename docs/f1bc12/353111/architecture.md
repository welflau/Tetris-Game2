# 架构设计 - Tetromino方块系统开发

## 架构模式
模块化组件架构

## 技术栈

- **language**: JavaScript ES6+
- **framework**: 原生JavaScript

## 模块设计

### TetrominoFactory
职责: 管理7种Tetromino方块类型的定义和创建
- createTetromino(type)
- getRandomTetromino()
- getAllTypes()

### TetrominoShape
职责: 单个Tetromino方块的数据结构和基础操作
- constructor(type, matrix, color)
- getMatrix()
- getColor()
- getType()
- clone()

### RotationSystem
职责: 处理方块旋转逻辑和旋转状态管理
- rotateClockwise(matrix)
- rotateCounterClockwise(matrix)
- getRotationStates(type)
- validateRotation(matrix, position, gameBoard)

### TetrominoGenerator
职责: 实现7-bag随机生成算法，确保方块分布均匀
- getNext()
- peek(count)
- refillBag()
- reset()

## 数据流
TetrominoFactory定义7种方块类型的矩阵数据和颜色 -> TetrominoGenerator使用7-bag算法生成随机序列 -> 创建TetrominoShape实例 -> RotationSystem处理旋转变换 -> 返回可用的方块对象给游戏引擎

## 关键决策
- 采用标准SRS(Super Rotation System)旋转系统确保兼容性
- 使用4x4矩阵统一表示所有方块类型，简化数据结构
- 实现7-bag随机算法避免连续出现相同方块
- 方块颜色采用标准Tetris配色方案提升用户体验
- 预生成旋转状态矩阵优化运行时性能
