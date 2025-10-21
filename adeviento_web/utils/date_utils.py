from datetime import datetime, timezone

def is_day_unlocked(day_number: int) -> bool:
    """
    Verifica si un día del calendario está desbloqueado.
    Los días se desbloquean a partir del 1 de diciembre de 2025.
    """
    # Fecha de inicio: 1 de diciembre de 2025
    start_date = datetime(2025, 12, 1, 0, 0, 0, tzinfo=timezone.utc)
    current_date = datetime.now(timezone.utc)
    
    # Calcular el día objetivo
    target_date = datetime(2025, 12, day_number, 0, 0, 0, tzinfo=timezone.utc)
    
    # El día está desbloqueado si la fecha actual es >= al día objetivo
    return current_date >= target_date

def get_days_until_unlock(day_number: int) -> int:
    """
    Calcula cuántos días faltan para que se desbloquee un día específico.
    """
    target_date = datetime(2025, 12, day_number, 0, 0, 0, tzinfo=timezone.utc)
    current_date = datetime.now(timezone.utc)
    
    time_diff = target_date - current_date
    days_until = time_diff.days
    
    return max(0, days_until)

def get_current_advent_day() -> int:
    """
    Obtiene el día actual del adviento (1-25).
    Retorna 0 si aún no es diciembre de 2025.
    """
    current_date = datetime.now(timezone.utc)
    
    # Solo en diciembre de 2025
    if current_date.year != 2025 or current_date.month != 12:
        return 0
    
    day = current_date.day
    return day if 1 <= day <= 25 else 0
