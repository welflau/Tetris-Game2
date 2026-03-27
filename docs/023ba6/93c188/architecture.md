# 架构设计 - 实现Board类 - 游戏面板管理

## 架构模式
MVC模式 + 面向对象设计

## 技术栈

- **language**: JavaScript (ES6+)
- **framework**: 原生JavaScript + HTML5 Canvas
- **database**: 无（客户端游戏）
- **others**: HTML5 Canvas API, CSS3, 模块化设计

## 模块设计

### Board类
职责: 游戏面板状态管理、网格操作、边界检测、行消除逻辑
- constructor(width, height) - 初始化面板
- getCell(x, y) - 获取指定位置状态
- setCell(x, y, value) - 设置指定位置状态
- isValidPosition(x, y) - 检查位置是否有效
- isOccupied(x, y) - 检查位置是否被占用
- placeTetromino(tetromino) - 放置方块到面板
- checkFullRows() - 检查满行
- clearRows(rows) - 清除指定行
- getBoard() - 获取面板状态副本
- reset() - 重置面板
- render(ctx) - 渲染面板到Canvas

### GridCell类
职责: 单个网格单元状态管理
- constructor(isEmpty, color) - 初始化单元格
- isEmpty() - 检查是否为空
- setColor(color) - 设置颜色
- getColor() - 获取颜色
- clear() - 清空单元格

### BoardRenderer类
职责: 面板渲染逻辑分离
- renderGrid(ctx, board) - 渲染网格线
- renderCells(ctx, board) - 渲染已占用单元格
- renderBackground(ctx) - 渲染背景

## 数据流
Board类维护二维数组表示游戏面板状态，每个位置存储GridCell对象。Game类通过Board接口进行网格操作，Tetromino类通过Board验证移动合法性。渲染时Board将状态数据传递给Canvas进行绘制。行消除时Board检测满行并更新内部状态，通知Game类更新分数。

## 风险点
- 二维数组索引越界风险
- 行消除时数组操作性能问题
- Canvas渲染频率过高导致性能下降
- 网格坐标系与Canvas坐标系转换错误

## 关键决策
- 使用二维数组存储网格状态，便于索引和遍历
- 采用GridCell对象封装单元格状态，提高可维护性
- 将渲染逻辑分离到BoardRenderer，遵循单一职责原则
- 使用深拷贝返回面板状态，避免外部直接修改内部数据
- 行消除采用splice操作配合unshift，保证性能
- 坐标系统采用左上角为原点，x向右y向下的标准Canvas坐标系
