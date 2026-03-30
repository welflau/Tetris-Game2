# 架构设计 - Tetromino方块系统开发

## 架构模式
MVC + 组件化架构

## 技术栈

- **language**: JavaScript ES6+
- **framework**: 原生JavaScript + HTML5 Canvas
- **database**: LocalStorage
- **others**: CSS3, Web Audio API, requestAnimationFrame

## 模块设计

### TetrominoFactory
职责: 负责创建和管理7种Tetromino方块类型的工厂类
- createTetromino(type)
- getRandomTetromino()
- getAllTypes()

### Tetromino
职责: 方块实体类，包含形状数据、位置、颜色和基础操作
- rotate()
- move(dx, dy)
- getShape()
- getColor()
- clone()

### TetrominoRenderer
职责: 负责方块的Canvas渲染，包括主游戏区和预览区
- render(tetromino, context)
- renderPreview(tetromino, context)
- renderGhost(tetromino, context)

### ShapeDefinitions
职责: 存储7种方块的形状矩阵定义和旋转状态
- getShapeMatrix(type, rotation)
- getColor(type)
- getRotationStates(type)

### TetrominoController
职责: 处理方块的用户输入控制和自动下落逻辑
- handleInput(keyCode)
- autoFall()
- pause()
- resume()

## 数据流
ShapeDefinitions提供方块定义 -> TetrominoFactory根据定义创建方块实例 -> Tetromino实例包含位置和状态数据 -> TetrominoController处理用户输入更新方块状态 -> TetrominoRenderer将方块状态渲染到Canvas

## 风险点
- 方块旋转时的边界检测复杂性
- Canvas渲染性能优化
- 不同方块类型的碰撞检测准确性
- 方块预览功能的同步更新

## 关键决策
- 使用工厂模式创建方块实例，便于扩展新方块类型
- 采用二维数组表示方块形状，支持4个旋转状态
- 分离渲染逻辑到独立模块，提高代码可维护性
- 使用requestAnimationFrame确保流畅的动画效果
- 实现方块克隆功能支持幽灵方块预览
