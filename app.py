import plotly.express as px
from shiny.express import input, ui, render
from shinywidgets import render_plotly, render_widget
import pandas as pd
import palmerpenguins
import seaborn as sns

penguins_df = palmerpenguins.load_penguins()

with ui.sidebar(position="left", open="open"):
    ui.h2("Sidebar")
    ui.input_selectize(
        "selected_attribute",
        "Attribute",
        choices=["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"],
    )
    ui.input_numeric("plotly_bin_count", "Plotly Count", value=25)
    ui.input_slider("seaborn_bin_count", "Seaborn Bins", 1, 100, 50)
    ui.input_checkbox_group(
        "selected_species_list",
        "Species",
        choices=["Adelie", "Gentoo", "Chinstrap"],
        selected="Adelie",
        inline=False,
    )
    ui.hr()
    ui.a(
        "Jeremy's GitHub",
        href="https://github.com/jfrummel/cintel-02-data",
        target="_blank",
    )

# Main Content

ui.page_opts(title="Jeremy's Penguin Histogram", fillable=False)
with ui.layout_columns():
    with ui.card(full_screen=True):
        ui.card_header("Data Table")

        @render.data_frame
        def penguins_table():
            return render.DataTable(penguins_df, selection_mode="row", width="300px", height="250px")

    with ui.card(full_screen=True):
        ui.card_header("Data Grid")

        @render.data_frame
        def penguins_grid():
            return render.DataGrid(penguins_df, filters=False, selection_mode="row", width="300px", height="250px")


with ui.layout_columns():
    with ui.card(full_screen=True):
        ui.card_header("Plotly Histogram")

        @render_widget
        def plot_1():
            histo = px.histogram(
                penguins_df,
                x="body_mass_g",
                nbins=input.plotly_bin_count(),color="species"
            ).update_layout(
                title={"text": "Penguin Mass", "x": 0.5},
                yaxis_title="Count",
                xaxis_title="Body Mass (g)",
            )

            return histo

    with ui.card(full_screen=True):
        ui.card_header("Seaborn Histogram")

        @render.plot(alt="A Seaborn histogram on penguin body mass in grams.")
        def plot_2():
            ax = sns.histplot(
                penguins_df, x="body_mass_g", bins=input.seaborn_bin_count(), hue="species"
            )
            ax.set_title("Palmer Penguins")
            ax.set_xlabel("Mass (g)")
            ax.set_ylabel("Count")
            return ax


with ui.layout_columns():
    with ui.card(full_screen=True):
        ui.card_header("Plotly Scatterplot: Species")

        @render_plotly
        def plotly_scatterplot():
            scatterplot = px.scatter(
                penguins_df, x="body_mass_g", y="bill_length_mm", color="species"
            ).update_layout(
                title={"text": "Bill Length vs Penguin Mass"},
                yaxis_title="Bill Length (mm)",
                xaxis_title="Body Mass (g)",
            )
            return scatterplot
