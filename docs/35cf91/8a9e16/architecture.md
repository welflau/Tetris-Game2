# 架构设计 - 自动化视觉回归测试

## 架构模式
测试驱动架构（TDD）+ 页面对象模式（Page Object Pattern）

## 技术栈

- **language**: JavaScript/TypeScript
- **framework**: Jest + Puppeteer/Playwright
- **database**: 无需数据库
- **others**: Canvas API, WebGL, Image Comparison Library (Pixelmatch), CI/CD Pipeline

## 模块设计

### VisualTestFramework
职责: 提供视觉回归测试的核心框架，包括截图对比、基准图像管理
- captureScreenshot()
- compareImages()
- updateBaseline()
- generateReport()

### GameStateManager
职责: 管理游戏状态设置，模拟各种游戏场景和方块配置
- setGameState()
- createTestScenario()
- resetGame()
- injectTestData()

### GhostPieceValidator
职责: 专门验证投影方块的显示效果，包括透明度、位置、颜色等
- validateGhostTransparency()
- checkGhostPosition()
- verifyGhostVisibility()

### CanvasAnalyzer
职责: 分析Canvas渲染内容，提取像素数据进行精确的视觉验证
- extractPixelData()
- analyzeTransparency()
- detectShapeOutline()
- measureContrast()

### TestScenarioBuilder
职责: 构建各种测试场景，包括不同背景、方块类型、游戏状态组合
- buildScenario()
- generateTestCases()
- createVariations()

### ReportGenerator
职责: 生成详细的测试报告，包括视觉差异对比和问题定位
- generateVisualReport()
- createDiffImages()
- exportResults()

## 数据流
测试执行器启动 → GameStateManager设置测试场景 → 游戏渲染投影方块 → CanvasAnalyzer提取像素数据 → GhostPieceValidator验证显示效果 → VisualTestFramework进行截图对比 → ReportGenerator生成测试报告 → CI/CD系统接收结果

## 风险点
- 不同浏览器和设备的渲染差异可能导致误报
- Canvas像素级对比的性能开销较大
- 基准图像的维护成本随测试用例增加而上升
- 透明度效果在不同显示器上的视觉差异
- 游戏动画和时序可能影响截图的一致性

## 关键决策
- 选择Playwright作为主要测试框架，支持多浏览器一致性测试
- 使用Pixelmatch进行像素级图像对比，提供可配置的容差阈值
- 实现分层测试策略：单元测试验证渲染逻辑，集成测试验证视觉效果
- 建立基准图像版本管理机制，支持渐进式更新
- 集成到CI/CD流水线，在代码变更时自动触发视觉回归测试
- 使用Canvas 2D Context的getImageData API进行精确的像素分析
- 实现测试用例参数化，覆盖多种游戏状态和设备配置组合
