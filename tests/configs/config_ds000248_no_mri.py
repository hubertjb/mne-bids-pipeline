"""
MNE Sample Data: Using the `fsaverage` template MRI
"""

study_name = 'ds000248'
bids_root = '~/mne_data/ds000248'
deriv_root = '~/mne_data/derivatives/mne-bids-pipeline/ds000248_no_mri'
subjects_dir = f'{bids_root}/derivatives/freesurfer/subjects'

subjects = ['01']
rename_events = {'Smiley': 'Emoji',
                 'Button': 'Switch'}
conditions = ['Auditory', 'Visual', 'Auditory/Left', 'Auditory/Right']
contrasts = [('Auditory/Right', 'Auditory/Left')]

ch_types = ['meg']
use_maxwell_filter = False
process_er = False

use_template_mri = True
