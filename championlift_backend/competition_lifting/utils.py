import math

# Coeficientes IPF GL (Classic Powerlifting, 2020-23) según PDF oficial
IPF_COEFFICIENTS = {
    'male': {'A': 1199.72839, 'B': 1025.18162, 'C': 0.00921},
    'female': {'A': 610.32796, 'B': 1045.59282, 'C': 0.03048},
}

def ipf_gl_points(weight_lifted: float, bodyweight: float, gender: str) -> float:
    """
    Calcula el puntaje IPF GL para un levantamiento individual con la fórmula:
    IPFC = (100 / (A - B * exp(-C * bodyweight))) * weight_lifted
    """
    coeffs = IPF_COEFFICIENTS.get(gender.lower())
    if not coeffs or bodyweight <= 0 or weight_lifted <= 0:
        return 0.0

    A = coeffs['A']
    B = coeffs['B']
    C = coeffs['C']

    denominator = A - B * math.exp(-C * bodyweight)
    if denominator == 0:
        return 0.0  # evitar división por cero

    points = (100 / denominator) * weight_lifted
    return round(points, 3)


def get_best_lifts(lift_history):
    """
    Obtiene los mejores levantamientos válidos para squat, bench y deadlift.
    Nombres normalizados a minúsculas.
    """
    squat_names = {'cuclilla', 'squad', 'squat', 'cuclilla(squad)'}
    bench_names = {'press de banca', 'bench', 'bench press'}
    deadlift_names = {'peso muerto', 'deadlift'}

    best = {'squat': 0.0, 'bench': 0.0, 'deadlift': 0.0}

    for lift in lift_history:
        if lift.valid != 'valid':
            continue
        lname = lift.name.strip().lower()
        if lname in squat_names:
            best['squat'] = max(best['squat'], lift.weight)
        elif lname in bench_names:
            best['bench'] = max(best['bench'], lift.weight)
        elif lname in deadlift_names:
            best['deadlift'] = max(best['deadlift'], lift.weight)

    return best

