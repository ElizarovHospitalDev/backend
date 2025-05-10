from rest_framework.routers import SimpleRouter

from api.v1.treatments import views


router = SimpleRouter()

router.register('microfloras', views.MicrofloraViewSet)
router.register('analysis-datas', views.AnalysisDataViewSet)
router.register('comobrid-pathologies', views.ComorbidPathologyViewSet)
router.register('outcome', views.TreatmentOutcomeViewSet)
router.register('surgical-interventions', views.SurgicalInterventionViewSet)
router.register('patients', views.PatientViewSet)
router.register('operations-stages', views.OperationStageViewSet)
router.register('arthroplasty_form', views.ArthroplastyFormViewSet)
router.register('', views.TreatmentViewSet)


urlpatterns = router.urls
