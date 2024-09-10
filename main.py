import pandas as pd
import matplotlib.pyplot as plt

# Clase principal para manejar el análisis de datos
class DataAnalyzer:
    def __init__(self, csv_file):
        self.data = pd.read_csv(csv_file, delimiter=",")
        self.salary = self.data["salary"]
        self.performance_score = self.data["performance_score"]
        self.departament = self.data["departament"]

    def calcular_media(self, columna):
        return columna.mean()

    def calcular_mediana(self, columna):
        len_columna = len(columna)
        if len_columna % 2 == 0:
            mitad1 = columna[len_columna // 2]
            mitad2 = columna[len_columna // 2 - 1]
            return (mitad1 + mitad2) / 2
        else:
            return columna[len_columna // 2]

    def calcular_desvio_estandar(self, columna):
        return columna.std()

    def empleados_por_departamento(self):
        return self.data["departament"].value_counts()

    def correlacion(self, columna1, columna2):
        return self.data[columna1].corr(self.data[columna2])

    def graficar_histograma(self):
        departamentos = self.data["departament"].unique()
        for departamento in departamentos:
            subset = self.data[self.data["departament"] == departamento]
            plt.hist(subset["performance_score"], bins=10, alpha=0.5, label=departamento)
        plt.xlabel('Performance Score')
        plt.ylabel('Frequency')
        plt.title('Histograma del Performance Score por Departamento')
        plt.legend(loc='upper right')
        plt.show()

    def graficar_dispersion(self, columna_x, columna_y):
        plt.scatter(self.data[columna_x], self.data[columna_y], alpha=0.5)
        plt.xlabel(columna_x)
        plt.ylabel(columna_y)
        plt.title(f'{columna_x} vs. {columna_y}')
        plt.show()

# Uso de la clase
if __name__ == "__main__":
    analyzer = DataAnalyzer('MOCK_DATA.csv')

    # Análisis de performance
    media_performance = analyzer.calcular_media(analyzer.performance_score)
    mediana_performance = analyzer.calcular_mediana(analyzer.performance_score)
    desvio_performance = analyzer.calcular_desvio_estandar(analyzer.performance_score)
    print("La media de Performance Score es:", media_performance)
    print("La mediana de Performance Score es:", mediana_performance)
    print("El desvío estándar de Performance Score es:", desvio_performance)

    # Análisis de salario
    media_salary = analyzer.calcular_media(analyzer.salary)
    mediana_salary = analyzer.calcular_mediana(analyzer.salary)
    desvio_salary = analyzer.calcular_desvio_estandar(analyzer.salary)
    print("La media de Salary es:", media_salary)
    print("La mediana de Salary es:", mediana_salary)
    print("El desvío estándar de Salary es:", desvio_salary)

    # Cantidad de empleados por departamento
    empleados_departamento = analyzer.empleados_por_departamento()
    print("Cantidad de empleados por departamento:", empleados_departamento)

    # Correlaciones
    correlacion_years_performance = analyzer.correlacion("years_with_company", "performance_score")
    correlacion_salary_performance = analyzer.correlacion("salary", "performance_score")
    print("Correlación entre Years With Company y Performance Score:", correlacion_years_performance)
    print("Correlación entre Salary y Performance Score:", correlacion_salary_performance)

    # Gráficos
    analyzer.graficar_histograma()
    analyzer.graficar_dispersion("years_with_company", "performance_score")
    analyzer.graficar_dispersion("salary", "performance_score")
