// Pie Chart and CSV Export Functionality

class PieChart {
    constructor(canvasId, data, colors) {
        this.canvasId = canvasId;
        this.canvas = document.getElementById(canvasId);
        
        if (!this.canvas) {
            console.error(`Canvas with ID ${canvasId} not found`);
            return false;
        }
        
        this.ctx = this.canvas.getContext('2d');
        this.data = data || [];
        this.colors = colors || [];
        
        // Wait for canvas to be fully rendered
        setTimeout(() => this.initialize(), 50);
    }
    
    initialize() {
        // Get actual canvas dimensions
        const rect = this.canvas.getBoundingClientRect();
        this.canvas.width = rect.width;
        this.canvas.height = rect.height;
        
        // Set DPI scaling for high-res displays
        const dpr = window.devicePixelRatio || 1;
        this.canvas.width = rect.width * dpr;
        this.canvas.height = rect.height * dpr;
        
        if (this.ctx) {
            this.ctx.scale(dpr, dpr);
        }
        
        this.centerX = (rect.width) / 2;
        this.centerY = (rect.height) / 2;
        this.radius = Math.min(rect.width, rect.height) / 2 - 30;
        
        if (this.data && this.data.length > 0) {
            this.draw();
        } else {
            console.warn(`No data provided for chart ${this.canvasId}`);
        }
    }

    draw() {
        if (!this.ctx || !this.data || this.data.length === 0) {
            return;
        }
        
        // Clear canvas with white background
        this.ctx.fillStyle = '#ffffff';
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
        
        const total = this.data.reduce((sum, item) => sum + item.value, 0);
        let currentAngle = -Math.PI / 2;

        this.data.forEach((item, index) => {
            if (!item.value) return;
            
            const sliceAngle = (item.value / total) * 2 * Math.PI;
            const color = this.colors[index] || '#999999';
            
            // Draw slice
            this.ctx.beginPath();
            this.ctx.moveTo(this.centerX, this.centerY);
            this.ctx.arc(this.centerX, this.centerY, this.radius, currentAngle, currentAngle + sliceAngle);
            this.ctx.lineTo(this.centerX, this.centerY);
            this.ctx.fillStyle = color;
            this.ctx.fill();
            
            // Draw border
            this.ctx.strokeStyle = '#ffffff';
            this.ctx.lineWidth = 3;
            this.ctx.stroke();

            // Draw percentage label
            const labelAngle = currentAngle + sliceAngle / 2;
            const labelX = this.centerX + Math.cos(labelAngle) * (this.radius * 0.65);
            const labelY = this.centerY + Math.sin(labelAngle) * (this.radius * 0.65);

            const percentage = item.percentage || Math.round((item.value / total) * 100);
            
            this.ctx.fillStyle = '#ffffff';
            this.ctx.font = 'bold 18px Arial, sans-serif';
            this.ctx.textAlign = 'center';
            this.ctx.textBaseline = 'middle';
            
            // Add shadow to text
            this.ctx.shadowColor = 'rgba(0,0,0,0.3)';
            this.ctx.shadowBlur = 4;
            this.ctx.fillText(percentage + '%', labelX, labelY);
            this.ctx.shadowColor = 'transparent';

            currentAngle += sliceAngle;
        });
    }

    getData() {
        return this.data;
    }
}

// CSV Export Function
function downloadCSV(data, filename, title = '') {
    let csv = '';
    
    if (title) {
        csv += title + '\n\n';
    }

    // Headers
    if (data && data.length > 0) {
        const headers = Object.keys(data[0]);
        csv += headers.join(',') + '\n';

        // Rows
        data.forEach(row => {
            const values = headers.map(header => {
                const value = row[header];
                // Escape quotes and wrap in quotes if contains comma
                if (typeof value === 'string' && value.includes(',')) {
                    return '"' + value.replace(/"/g, '""') + '"';
                }
                return value;
            });
            csv += values.join(',') + '\n';
        });
    }

    // Create blob and download
    const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
    const link = document.createElement('a');
    const url = URL.createObjectURL(blob);
    
    link.setAttribute('href', url);
    link.setAttribute('download', filename);
    link.style.visibility = 'hidden';
    
    document.body.appendChild(link);
    
    try {
        link.click();
    } catch (e) {
        console.error('Download failed:', e);
    }
    
    document.body.removeChild(link);
    
    // Clean up
    URL.revokeObjectURL(url);
}

// Initialize CSV export buttons
function initCSVButtons() {
    const csvButtons = document.querySelectorAll('.csv-export-button');
    csvButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            
            const targetId = this.getAttribute('data-target');
            const filename = this.getAttribute('data-filename') || 'dados.csv';
            const title = this.getAttribute('data-title') || '';
            
            if (targetId && window.pieCharts && window.pieCharts[targetId]) {
                const chart = window.pieCharts[targetId];
                if (typeof chart.getData === 'function') {
                    const data = chart.getData();
                    downloadCSV(data, filename, title);
                }
            }
        });
    });
}

// Initialize on document ready
function initPieCharts() {
    initCSVButtons();
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initPieCharts);
} else {
    initPieCharts();
}

// Store pie charts globally for access
window.pieCharts = window.pieCharts || {};
