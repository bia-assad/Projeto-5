def plot_graph(df,column):            
    avg_price_by_variable = df.groupby(column)['price'].mean().reset_index()       
    fig = px.scatter(df, x=column, y='price', title=f'Price Distribution by {column}')
    fig.update_layout(xaxis=dict(dtick=2))
    
 return fig