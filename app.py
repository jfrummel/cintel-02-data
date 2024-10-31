import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly
import palmerpenguins

penguins_df = palmerpenguins.load_penguins()

with ui.sidebar(position="left", open="open"):
    ui.h2("Sidebar")
    ui.input_selectize(
        "selected_attribute",
        "Attribute",
        choices=["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"],
    )
    ui.input_numeric("plotly_bin_count", "Plotly Count", value=2)
    ui.input_slider("seaborn_bin_count", "Seaborn Bins", 1, 100, 50)
    ui.input_checkbox_group(
        "selected_species_list",
        "Species",
        choices=["Adelie", "Gentoo", "Chinstrap"],
        selected="Adelie",
        inline=False,
    )
    ui.hr()
    ui.a("Jeremy's GitHub", href="https://github.com/jfrummel/cintel-02-data", target= "_blank")
ui.page_opts(title="Jeremy's Penguin Histogram", fillable=True)
with ui.layout_columns():

    @render_plotly
    def plot1():
        return px.histogram(px.data.tips(), y="tip")
