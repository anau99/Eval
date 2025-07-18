import plotly.graph_objects as go
import plotly.io as pio
import pandas as pd
import os


try:
    metrics_data = pd.read_csv("./data/firstdata.csv")
except FileNotFoundError:
    print("❌ Error: File firstdata.csv not found. Please run data_gen.py first.")
    exit(1)

metrics_html = ""
for _, row in metrics_data.iterrows():
    change_class = "text-success" if row["ChangeType"] == "positive" else "text-danger"
    change_icon = "+" if row["ChangeType"] == "positive" else ""
    

    prefix = str(row["Prefix"]) if pd.notna(row["Prefix"]) else ""
    
    metrics_html += """
    <div class="col-md-3">
        <div class="dashboard-card">
            <div class="card-body">
                <h6>""" + row["Title"] + """</h6>
                <h3 class="metric-value">""" + prefix + str("{:,}".format(row["Value"])) + """</h3>
                <p class=\"""" + change_class + """ mb-0">""" + change_icon + str(row["Change"]) + """%</p>
            </div>
        </div>
    </div>
    """

projects_data = pd.read_csv("./data/projects.csv")
projects_html = ""
for _, row in projects_data.iterrows():
    members = "".join([f'<span class="avatar">{m}</span>' for m in row["Members"].split(",")])
    
    projects_html += f"""
    <div class="project-item">
        <h6>{row["ProjectName"]}</h6>
        <div class="avatar-group mt-2">
            {members}
        </div>
        <div class="mt-2">
            <div class="progress">
                <div class="progress-bar" style="width: {row["ProgressPercent"]}"></div>
            </div>
            <div class="d-flex justify-content-between mt-1">
                <span class="text-sm">{row["Budget"]}</span>
                <span class="text-sm">{row["ProgressPercent"]}</span>
            </div>
        </div>
    </div>
    """

def generate_orders_html_from_csv():
    """Đọc file orders.csv và tạo HTML bằng string concatenation"""
    try:

        orders_data = pd.read_csv("./data/orders.csv")
        

        orders_html = ""

        for _, row in orders_data.iterrows():
            orders_html += """
            <div class="order-item">
                <span class="order-icon """ + row['IconClass'] + """">
                    <i class="fas """ + row['Icon'] + """></i>
                </span>
                <h6 class="mb-1">""" + row['Title'] + """</h6>
                <p class="text-sm text-muted mb-0">""" + row['Date'] + """</p>
            </div>
            """
        
        return orders_html
    
    except Exception as e:
        print(f"❌ Lỗi khi đọc file orders.csv: {str(e)}")
        return """
        <div class="order-item">
            <span class="order-icon bg-success">
                <i class="fas fa-bell"></i>
            </span>
            <h6 class="mb-1">$2400, Design changes</h6>
            <p class="text-sm text-muted mb-0">22 DEC 7:20 PM</p>
        </div>
        <!-- Các order mặc định khác -->
        """

def get_order_data():
    """Đọc file CSV và trả về từng giá trị riêng biệt"""
    try:
        df = pd.read_csv("./data/orders.csv")
        return {
            # Order 1
            "order1_iconclass": df.iloc[0]['IconClass'],
            "order1_icon": df.iloc[0]['Icon'],
            "order1_title": df.iloc[0]['Title'],
            "order1_date": df.iloc[0]['Date'],
            
            # Order 2
            "order2_iconclass": df.iloc[1]['IconClass'],
            "order2_icon": df.iloc[1]['Icon'],
            "order2_title": df.iloc[1]['Title'],
            "order2_date": df.iloc[1]['Date'],
            
            # Order 3
            "order3_iconclass": df.iloc[2]['IconClass'],
            "order3_icon": df.iloc[2]['Icon'],
            "order3_title": df.iloc[2]['Title'],
            "order3_date": df.iloc[2]['Date'],
            
            # Order 4
            "order4_iconclass": df.iloc[3]['IconClass'],
            "order4_icon": df.iloc[3]['Icon'],
            "order4_title": df.iloc[3]['Title'],
            "order4_date": df.iloc[3]['Date'],
            
            # Order 5
            "order5_iconclass": df.iloc[4]['IconClass'],
            "order5_icon": df.iloc[4]['Icon'],
            "order5_title": df.iloc[4]['Title'],
            "order5_date": df.iloc[4]['Date'],
            
            # Order 6
            "order6_iconclass": df.iloc[5]['IconClass'],
            "order6_icon": df.iloc[5]['Icon'],
            "order6_title": df.iloc[5]['Title'],
            "order6_date": df.iloc[5]['Date']
        }
    except Exception as e:
        print(f"Error reading orders.csv: {e}")
        return None

order_data = get_order_data()
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <title>Dashboard</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
  <style>
    body {
      background-color: #f8f9fa;
    }
    .dashboard-card {
      border-radius: 12px;
      box-shadow: 0 4px 6px rgba(0,0,0,0.1);
      margin-bottom: 24px;
      height: 100%;
      background-color: white;
    }
    .card-header {
      padding: 16px 24px;
      border-bottom: 1px solid rgba(0,0,0,0.1);
    }
    .card-body {
      padding: 24px;
    }
    .chart-container {
      height: 200px;
    }
    .metric-value {
      font-size: 28px;
      font-weight: 600;
    }
    .text-success {
      color: #4CAF50 !important;
    }
    .text-danger {
      color: #F44336 !important;
    }
    .project-item {
      padding: 12px 0;
      border-bottom: 1px solid #eee;
    }
    .project-item:last-child {
      border-bottom: none;
    }
    .order-item {
      padding: 12px 0;
      border-bottom: 1px solid #eee;
      position: relative;
      padding-left: 40px;
    }
    .order-item:last-child {
      border-bottom: none;
    }
    .order-icon {
      position: absolute;
      left: 0;
      width: 30px;
      height: 30px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      color: white;
    }
    .progress {
      height: 6px;
      background-color: #e9ecef;
      border-radius: 3px;
    }
    .progress-bar {
      background-color: #4CAF50;
    }
    .avatar {
      width: 24px;
      height: 24px;
      border-radius: 50%;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      color: white;
      font-size: 12px;
      margin-right: 4px;
    }
    .bg-primary { background-color: #4CAF50; }
    .bg-success { background-color: #66BB6A; }
    .bg-info { background-color: #26C6DA; }
    .bg-warning { background-color: #FFA726; }
    .bg-danger { background-color: #EF5350; }
  </style>
</head>
<body>
  <div class="container-fluid py-4">
    <div class="row mb-4">
      <div class="col-12">
        <h1>Dashboard</h1>
      </div>
    </div>

    <!-- Metrics Row -->
    <div class="row mb-4">
""" + metrics_html + """
    </div>

    <!-- Charts Row -->
    <div class="row">
      <!-- Website Views -->
      <div class="col-md-4">
        <div class="dashboard-card">
          <div class="card-header">
            <h5 class="mb-0">Website Views</h5>
            <p class="text-sm mb-0">Last Campaign Performance</p>
          </div>
          <div class="card-body">
            <div id="chart-bars" class="chart-container"></div>
            <hr>
            <div class="d-flex align-items-center">
              <i class="fas fa-clock me-2"></i>
              <p class="mb-0 text-sm">campaign sent 2 days ago</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Daily Sales -->
      <div class="col-md-4">
        <div class="dashboard-card">
          <div class="card-header">
            <h5 class="mb-0">Daily Sales</h5>
            <p class="text-sm mb-0">(<span class="font-weight-bolder text-success">+15%</span>) increase in today sales.</p>
          </div>
          <div class="card-body">
            <div id="chart-line" class="chart-container"></div>
            <hr>
            <div class="d-flex align-items-center">
              <i class="fas fa-clock me-2"></i>
              <p class="mb-0 text-sm">updated 4 min ago</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Completed Tasks -->
      <div class="col-md-4">
        <div class="dashboard-card">
          <div class="card-header">
            <h5 class="mb-0">Completed Tasks</h5>
            <p class="text-sm mb-0">Last Campaign Performance</p>
          </div>
          <div class="card-body">
            <div id="chart-line-tasks" class="chart-container"></div>
            <hr>
            <div class="d-flex align-items-center">
              <i class="fas fa-clock me-2"></i>
              <p class="mb-0 text-sm">just updated</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Bottom Row -->
    <div class="row mt-4">
      <!-- Projects -->
      <div class="col-lg-8">
        <div class="dashboard-card">
          <div class="card-header">
            <div class="row align-items-center">
              <div class="col">
                <h5 class="mb-0">Projects</h5>
                <p class="text-sm mb-0">
                  <i class="fas fa-check text-success me-1"></i>
                  <span class="font-weight-bold">30 done</span> this month
                </p>
              </div>
              <div class="col text-end">
                <button class="btn btn-sm btn-outline-secondary">
                  <i class="fas fa-ellipsis-v"></i>
                </button>
              </div>
            </div>
          </div>
          <div class="card-body">
            <div class="project-list">
                """ + projects_html + """
            </div>
          </div>
        </div>
      </div>

      <!-- Orders Overview -->
      <div class="col-lg-4">
        <div class="dashboard-card">
          <div class="card-header">
            <h5 class="mb-0">Orders overview</h5>
            <p class="text-sm mb-0">
              <i class="fas fa-arrow-up text-success me-1"></i>
              <span class="font-weight-bold text-success">24%</span> this month
            </p>
          </div>
          <div class="card-body">
            <div class="order-list">
              <div class="order-item">
                <span class="order-icon bg-success">
                  <i class="fas fa-bell"></i>
                </span>
                <h6 class="mb-1">"""+order_data['order1_title']+"""</h6>
                <p class="text-sm text-muted mb-0">"""+order_data['order1_date']+"""</p>
              </div>
              
              <div class="order-item">
                <span class="order-icon bg-danger">
                  <i class="fas fa-code"></i>
                </span>
                <h6 class="mb-1">"""+order_data['order2_title']+"""</h6>
                <p class="text-sm text-muted mb-0">"""+order_data['order2_date']+"""</p>
              </div>
              
              <div class="order-item">
                <span class="order-icon bg-info">
                  <i class="fas fa-shopping-cart"></i>
                </span>
                <h6 class="mb-1">"""+order_data['order3_title']+"""</h6>
                <p class="text-sm text-muted mb-0">"""+order_data['order3_date']+"""</p>
              </div>
              
              <div class="order-item">
                <span class="order-icon bg-warning">
                  <i class="fas fa-credit-card"></i>
                </span>
                <h6 class="mb-1">"""+order_data['order4_title']+"""</h6>
                <p class="text-sm text-muted mb-0">"""+order_data['order4_date']+"""</p>
              </div>
              
              <div class="order-item">
                <span class="order-icon bg-primary">
                  <i class="fas fa-unlock"></i>
                </span>
                <h6 class="mb-1">"""+order_data['order5_title']+"""</h6>
                <p class="text-sm text-muted mb-0">"""+order_data['order5_date']+"""</p>
              </div>
              
              <div class="order-item">
                <span class="order-icon bg-success">
                  <i class="fas fa-shopping-bag"></i>
                </span>
                <h6 class="mb-1">"""+order_data['order6_title']+"""</h6>
                <p class="text-sm text-muted mb-0">"""+order_data['order6_date']+"""</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
  
"""


try:
    views_data = pd.read_csv("./data/website_views.csv")
    x = views_data['Day'].tolist()
    y = views_data['Views'].tolist()
except FileNotFoundError:
    print("❌ Error: File website_views.csv not found. Using default data.")

# 1. Website Views (Bar Chart)
bar_chart = go.Figure(go.Bar(

    x = x,
    y = y,
    
    marker_color='#4CAF50'
))
bar_chart.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    margin=dict(l=20, r=20, t=20, b=20),
    showlegend=False,
    yaxis=dict(
        gridcolor='#e5e5e5',
        range=[0, 100],
        showticklabels=True
    ),
    xaxis=dict(showgrid=False)
)

# 2. Daily Sales (Line Chart)
sales_data = pd.read_csv("./data/daily_sales.csv")
line_chart = go.Figure(go.Scatter(
    x=sales_data['Month'].tolist(),
    y=sales_data['Sales'].tolist(),
    mode='lines',
    line=dict(color='#4CAF50', width=2),
    marker=dict(color='#4CAF50', size=6)
))
line_chart.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    margin=dict(l=20, r=20, t=20, b=20),
    showlegend=False,
    yaxis=dict(
        gridcolor='#e5e5e5',
        range=[0, 500],
        showticklabels=True
    ),
    xaxis=dict(showgrid=False)
)

# 3. Completed Tasks (Line Chart)
tasks_data = pd.read_csv("./data/completed_tasks.csv")
tasks_chart = go.Figure(go.Scatter(
    x=tasks_data['Month'].tolist(),
    y=tasks_data['Tasks'].tolist(),
    mode='lines+markers',
    line=dict(color='#4CAF50', width=2),
    marker=dict(color='#4CAF50', size=6)
))
tasks_chart.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    margin=dict(l=20, r=20, t=20, b=20),
    showlegend=False,
    yaxis=dict(
        gridcolor='#e5e5e5',
        range=[0, 600],
        showticklabels=True
    ),
    xaxis=dict(showgrid=False)
)


html_content += """
  <script>
    Plotly.newPlot('chart-bars', """ + pio.to_json(bar_chart) + """);
    Plotly.newPlot('chart-line', """ + pio.to_json(line_chart) + """);
    Plotly.newPlot('chart-line-tasks', """ + pio.to_json(tasks_chart) + """);
  </script>
</body>
</html>
"""

# HTML
with open('./outputs/dashboard.html', 'w') as f:
    f.write(html_content)

print("HTML file generated successfully!")