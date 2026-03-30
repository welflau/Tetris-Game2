/**
 * 响应式布局实现 - 前端模块
 * 由 AI 自动开发系统生成
 */

class ResponsiveLayout {
    constructor() {
        this.breakpoints = {
            mobile: 320,
            tablet: 768,
            desktop: 1024,
            large: 1200,
            xlarge: 1440
        };
        this.currentBreakpoint = null;
        this.init();
    }

    init() {
        this.detectBreakpoint();
        this.setupEventListeners();
        this.optimizeForDevice();
    }

    detectBreakpoint() {
        const width = window.innerWidth;
        let breakpoint = 'mobile';
        
        if (width >= this.breakpoints.xlarge) {
            breakpoint = 'xlarge';
        } else if (width >= this.breakpoints.large) {
            breakpoint = 'large';
        } else if (width >= this.breakpoints.desktop) {
            breakpoint = 'desktop';
        } else if (width >= this.breakpoints.tablet) {
            breakpoint = 'tablet';
        }
        
        if (this.currentBreakpoint !== breakpoint) {
            this.currentBreakpoint = breakpoint;
            this.onBreakpointChange(breakpoint);
        }
        
        return breakpoint;
    }

    setupEventListeners() {
        let resizeTimer;
        window.addEventListener('resize', () => {
            clearTimeout(resizeTimer);
            resizeTimer = setTimeout(() => {
                this.detectBreakpoint();
                this.handleResize();
            }, 100);
        });

        window.addEventListener('orientationchange', () => {
            setTimeout(() => {
                this.detectBreakpoint();
                this.handleOrientationChange();
            }, 100);
        });
    }

    onBreakpointChange(breakpoint) {
        document.body.setAttribute('data-breakpoint', breakpoint);
        
        // 触发自定义事件
        const event = new CustomEvent('breakpointChange', {
            detail: { breakpoint, width: window.innerWidth }
        });
        window.dispatchEvent(event);
        
        console.log(`断点变化: ${breakpoint} (${window.innerWidth}px)`);
    }

    handleResize() {
        // 处理窗口大小变化
        this.adjustFontSize();
        this.optimizeImages();
    }

    handleOrientationChange() {
        // 处理设备方向变化
        const orientation = screen.orientation ? screen.orientation.type : 
            (window.innerHeight > window.innerWidth ? 'portrait' : 'landscape');
        
        document.body.setAttribute('data-orientation', orientation);
        
        console.log(`方向变化: ${orientation}`);
    }

    adjustFontSize() {
        const width = window.innerWidth;
        let fontSize = 16;
        
        if (width < this.breakpoints.tablet) {
            fontSize = 14;
        } else if (width >= this.breakpoints.large) {
            fontSize = 18;
        }
        
        document.documentElement.style.fontSize = fontSize + 'px';
    }

    optimizeForDevice() {
        // 检测设备类型
        const isMobile = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
        const isTouch = 'ontouchstart' in window || navigator.maxTouchPoints > 0;
        
        if (isMobile || isTouch) {
            document.body.classList.add('touch-device');
            this.optimizeForTouch();
        }
        
        // 检测高分辨率屏幕
        if (window.devicePixelRatio > 1) {
            document.body.classList.add('high-dpi');
        }
        
        // 检测网络状况
        if ('connection' in navigator) {
            const connection = navigator.connection;
            if (connection.effectiveType === 'slow-2g' || connection.effectiveType === '2g') {
                document.body.classList.add('slow-connection');
                this.optimizeForSlowConnection();
            }
        }
    }

    optimizeForTouch() {
        // 为触摸设备优化交互
        const buttons = document.querySelectorAll('button, .btn, a');
        buttons.forEach(button => {
            const computedStyle = window.getComputedStyle(button);
            const minSize = 44; // 最小触摸目标尺寸
            
            if (parseInt(computedStyle.height) < minSize) {
                button.style.minHeight = minSize + 'px';
            }
            if (parseInt(computedStyle.width) < minSize) {
                button.style.minWidth = minSize + 'px';
            }
        });
    }

    optimizeImages() {
        const images = document.querySelectorAll('img');
        images.forEach(img => {
            if (!img.hasAttribute('data-responsive-optimized')) {
                img.style.maxWidth = '100%';
                img.style.height = 'auto';
                img.setAttribute('data-responsive-optimized', 'true');
            }
        });
    }

    optimizeForSlowConnection() {
        // 为慢速连接优化
        const images = document.querySelectorAll('img');
        images.forEach(img => {
            if (img.dataset.lowRes) {
                img.src = img.dataset.lowRes;
            }
        });
        
        // 禁用非必要动画
        document.body.classList.add('reduced-motion');
    }

    getCurrentBreakpoint() {
        return this.currentBreakpoint;
    }

    isBreakpoint(breakpoint) {
        return this.currentBreakpoint === breakpoint;
    }

    isMobile() {
        return this.currentBreakpoint === 'mobile';
    }

    isTablet() {
        return this.currentBreakpoint === 'tablet';
    }

    isDesktop() {
        return ['desktop', 'large', 'xlarge'].includes(this.currentBreakpoint);
    }

    getViewportInfo() {
        return {
            width: window.innerWidth,
            height: window.innerHeight,
            breakpoint: this.currentBreakpoint,
            orientation: window.innerHeight > window.innerWidth ? 'portrait' : 'landscape',
            devicePixelRatio: window.devicePixelRatio,
            isTouch: 'ontouchstart' in window
        };
    }

    render(container) {
        if (!container) return;
        
        container.innerHTML = `
            <div class="responsive-layout-info">
                <h3>响应式布局信息</h3>
                <div class="viewport-info">
                    <p>当前断点: <span id="current-breakpoint">${this.currentBreakpoint}</span></p>
                    <p>屏幕尺寸: <span id="screen-size">${window.innerWidth} x ${window.innerHeight}</span></p>
                    <p>设备像素比: <span id="device-ratio">${window.devicePixelRatio}</span></p>
                </div>
                <div class="breakpoint-indicators">
                    <div class="indicator ${this.isMobile() ? 'active' : ''}" data-breakpoint="mobile">移动端</div>
                    <div class="indicator ${this.isTablet() ? 'active' : ''}" data-breakpoint="tablet">平板</div>
                    <div class="indicator ${this.isDesktop() ? 'active' : ''}" data-breakpoint="desktop">桌面端</div>
                </div>
            </div>
        `;
        
        // 监听断点变化并更新显示
        window.addEventListener('breakpointChange', (e) => {
            const breakpointSpan = container.querySelector('#current-breakpoint');
            const screenSizeSpan = container.querySelector('#screen-size');
            const indicators = container.querySelectorAll('.indicator');
            
            if (breakpointSpan) {
                breakpointSpan.textContent = e.detail.breakpoint;
            }
            if (screenSizeSpan) {
                screenSizeSpan.textContent = `${e.detail.width} x ${window.innerHeight}`;
            }
            
            indicators.forEach(indicator => {
                indicator.classList.remove('active');
                if (indicator.dataset.breakpoint === e.detail.breakpoint || 
                    (e.detail.breakpoint === 'desktop' && indicator.dataset.breakpoint === 'desktop') ||
                    (e.detail.breakpoint === 'large' && indicator.dataset.breakpoint === 'desktop') ||
                    (e.detail.breakpoint === 'xlarge' && indicator.dataset.breakpoint === 'desktop')) {
                    indicator.classList.add('active');
                }
            });
        });
    }
}

// 自动初始化
if (typeof window !== 'undefined') {
    window.ResponsiveLayout = ResponsiveLayout;
    
    // 页面加载完成后自动初始化
    document.addEventListener('DOMContentLoaded', () => {
        window.responsiveLayout = new ResponsiveLayout();
    });
}

// 导出模块（如果支持）
if (typeof module !== 'undefined' && module.exports) {
    module.exports = ResponsiveLayout;
}