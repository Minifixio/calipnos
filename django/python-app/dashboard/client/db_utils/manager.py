from ..binary_utils import read as binary_read
from client.models import DeviceMeasure, DeviceMeasurePoint, DoctorConfigurationParameterName, DoctorConfigurationParameterValue
from django.http import JsonResponse
from collections import defaultdict
import datetime
import pytz

def convert_ms_to_datetime(seconds):
    # Convertir le timestamp en objet datetime
    date_time = datetime.datetime.fromtimestamp(seconds, tz=pytz.utc)
    return date_time

def add_measure(file_content):
    """
    Ajoute une nouvelle mesure à la base de données en parsant le contenu du fichier binaire.
    """
    # TODO: Ajouter la gestion d'erreurs de lecture binaires
    result = binary_read.read_binary_file(file_content)
    
    # Le format du résultat est le suivant:
    # result = {
    #     'timestamp_start': timestamp_start,
    #     'timestamp_stop': timestamp_stop,
    #     'version': version,
    #     'pta': pta,
    #     'measures': measures,
    #     'config': config,
    # }

    measure = DeviceMeasure(
        version=result['version'],
        config=result['config'],
        pta=result['pta'],
        start_time=convert_ms_to_datetime(result['timestamp_start']),
        end_time=convert_ms_to_datetime(result['timestamp_stop']),
        points_count=len(result['measures'])
    )
    measure.save()
    print(f"Saved measure with ID: {measure.id}")

    # Le format des mesures est le suivant:
    # measure = {
    #     timestamp,
    #     battery,
    #     integrity,
    #     spo2,
    #     heart_rate,
    #     odba,
    #     audio_sp1,
    #     audio_sp2,
    #     audio_sp3,
    #     audio_sp4,
    #     audio_sp5,
    #     audio_sp6,
    #     audio_sp7,
    #     audio_sp8,
    #     audio_sp9,
    #     audio_sp10
    # }

    for m in result['measures']:
        measure_point = DeviceMeasurePoint(
            measure=measure,
            timestamp=convert_ms_to_datetime(m['timestamp']),
            battery=m['battery'],
            integrity=m['integrity'],
            sp02=m['spo2'],
            bpm=m['heart_rate'],
            obda=m['odba'],
            audio_sp1=m['audio_sp1'],
            audio_sp2=m['audio_sp2'],
            audio_sp3=m['audio_sp3'],
            audio_sp4=m['audio_sp4'],
            audio_sp5=m['audio_sp5'],
            audio_sp6=m['audio_sp6'],
            audio_sp7=m['audio_sp7'],
            audio_sp8=m['audio_sp8'],
            audio_sp9=m['audio_sp9'],
            audio_sp10=m['audio_sp10']
        )
        measure_point.save()
    
    print(f"Saved {len(result['measures'])} measure points")

def get_measures():
    """
    Récupère toutes les mesures de la base de données.
    """
    measures = DeviceMeasure.objects.all()
    return measures

def get_measure(measure_id):
    """
    Récupère une mesure spécifique de la base de données.
    """
    try:
        measure = DeviceMeasure.objects.get(id=measure_id)
        return measure
    except DeviceMeasure.DoesNotExist:
        print("Trying to get a non-existing measure")
        return None
    
def delete_measure(measure_id):
    """
    Supprime une mesure de la base de données.
    """
    try:
        measure = DeviceMeasure.objects.get(id=measure_id)
        measure.delete()
        
        # Supprimer les points de mesure associés
        # TODO: Check si nécessaire
        measure_points = DeviceMeasurePoint.objects.filter(measure=measure)
        for point in measure_points:
            point.delete()
        return True
    except DeviceMeasure.DoesNotExist:
        print("Trying to delete a non-existing measure")
        return False
    
def get_measure_points(measure_id):
    """
    Récupère les points de mesure pour une mesure spécifique.
    """
    try:
        measure = DeviceMeasure.objects.get(id=measure_id)
        measure_points = DeviceMeasurePoint.objects.filter(measure=measure)
        return measure_points
    except DeviceMeasurePoint.DoesNotExist:
        print("Trying to get points for a non-existing measure")
        return None
    
def get_configurations():
        # Récupére les noms des paramètres depuis DoctorConfigurationParameterName
        # Pour chaque paramètre param_n, on récupére les valeurs des paramètres 
        # depuis DoctorConfigurationParameterValue pour lesquels param=param_n

        params_with_values = defaultdict(list)

        # Récupérer tous les paramètres
        parameters = DoctorConfigurationParameterName.objects.all()

        for param in parameters:
            # Récupérer les valeurs distinctes pour chaque paramètre
            values = DoctorConfigurationParameterValue.objects.filter(param=param).values_list('value', flat=True).distinct()

            # Ajouter au dictionnaire
            params_with_values[param.name] = list(values)
        
        return dict(params_with_values)
