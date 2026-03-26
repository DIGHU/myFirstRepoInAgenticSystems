import pandas as pd
import plotly.express as px

# Step 1: Create dataset
epochs = list(range(1, 11))
training_loss = [0.9, 0.75, 0.6, 0.5, 0.42, 0.38, 0.35, 0.34, 0.33, 0.32]

#dataframe
df = pd.DataFrame({
    "Epoch": epochs,
    "Loss": training_loss
})

fig = px.line(
    df,
    x="Epoch",
    y="Loss",
    title="Training Loss Over Epochs",
    markers=True
)

#  axis labels
fig.update_layout(
    xaxis_title="Epoch",
    yaxis_title="Training Loss"
)

#Add annotation
fig.add_annotation(
    x=7,
    y=0.35,
    text="Loss Stabilizing",
    showarrow=True,
    arrowhead=2
)

# chart
fig.show()