from collections import Counter
import pandas as pd


cov_selection = ['back-end developer', 'other', 'supervisor/team lead',
       'devops/sysadmin', 'front-end developer', 'age_group',
       'Does your employer provide mental health benefits as part of healthcare coverage?_no',
       'If a mental health issue prompted you to request a medical leave from work, asking for that leave would be:_i don\'t know',
       'If a mental health issue prompted you to request a medical leave from work, asking for that leave would be:_neither easy nor difficult',
       'If a mental health issue prompted you to request a medical leave from work, asking for that leave would be:_somewhat difficult',
       'If a mental health issue prompted you to request a medical leave from work, asking for that leave would be:_somewhat easy',
       'If a mental health issue prompted you to request a medical leave from work, asking for that leave would be:_very easy',
       'Do you think that discussing a mental health disorder with your employer would have negative consequences?_yes',
       'How willing would you be to share with friends and family that you have a mental illness?_somewhat not open',
       'How willing would you be to share with friends and family that you have a mental illness?_somewhat open',
       'How willing would you be to share with friends and family that you have a mental illness?_very open',
       'Do you have a family history of mental illness?_i don\'t know',
       'Have you had a mental health disorder in the past?_maybe',
       'Do you currently have a mental health disorder?_maybe',
       'If you have a mental health issue, do you feel that it interferes with your work when being treated effectively?_rarely',
       'If you have a mental health issue, do you feel that it interferes with your work when being treated effectively?_sometimes',
       'If you have a mental health issue, do you feel that it interferes with your work when NOT being treated effectively?_sometimes']

var_selection = ['Have you ever sought treatment for a mental health issue from a mental health professional?',
       'back-end developer', 'no diagnose', 'age_group',
       'Does your employer provide mental health benefits as part of healthcare coverage?_yes',
       'Do you know the options for mental health care available under your employer-provided coverage?_no',
       'Does your employer offer resources to learn more about mental health concerns and options for seeking help?_no',
       'Do you think that discussing a mental health disorder with your employer would have negative consequences?_maybe',
       'Do you think that discussing a mental health disorder with your employer would have negative consequences?_no',
       'Would you feel comfortable discussing a mental health disorder with your coworkers?_maybe',
       'Would you feel comfortable discussing a mental health disorder with your direct supervisor(s)?_yes',
       'Do you feel that your employer takes mental health as seriously as physical health?_i don\'t know',
       'Do you feel that being identified as a person with a mental health issue would hurt your career?_maybe',
       'Do you think that team members/co-workers would view you more negatively if they knew you suffered from a mental health issue?_maybe',
       'How willing would you be to share with friends and family that you have a mental illness?_somewhat open',
       'Do you have a family history of mental illness?_yes',
       'Have you had a mental health disorder in the past?_yes',
       'Do you currently have a mental health disorder?_no',
       'Do you currently have a mental health disorder?_yes',
       'Have you been diagnosed with a mental health condition by a medical professional?_no',
       'Have you been diagnosed with a mental health condition by a medical professional?_yes',
       'If you have a mental health issue, do you feel that it interferes with your work when being treated effectively?_not applicable to me',
       'Do you work remotely?_sometimes']

pca_selection = ['What is your gender?_aeeflm',
                 'Do you think that team members/co-workers would view you more negatively if they knew you suffered from a mental health issue?_yes, i think they would',
                 'Do you feel that being identified as a person with a mental health issue would hurt your career?_yes, i think it would',
                 "Do you think that team members/co-workers would view you more negatively if they knew you suffered from a mental health issue?_no, i don't think they would",
                 "Does your employer provide mental health benefits as part of healthcare coverage?_i don't know",
                 'Do you feel that being identified as a person with a mental health issue would hurt your career?_maybe',
                 'Would you feel comfortable discussing a mental health disorder with your coworkers?_no',
                 'Do you know the options for mental health care available under your employer-provided coverage?_yes',
                 'What is your gender?_m',
                 "Do you feel that being identified as a person with a mental health issue would hurt your career?_no, i don't think it would",
                 'Would you feel comfortable discussing a mental health disorder with your coworkers?_yes',
                 'Does your employer provide mental health benefits as part of healthcare coverage?_yes',
                 'Do you think that discussing a mental health disorder with your employer would have negative consequences?_yes',
                 'How willing would you be to share with friends and family that you have a mental illness?_very open',
                 'Do you currently have a mental health disorder?_no',
                 'Do you feel that being identified as a person with a mental health issue would hurt your career?_yes, it has',
                 'Do you currently have a mental health disorder?_yes',
                 'Do you think that team members/co-workers would view you more negatively if they knew you suffered from a mental health issue?_maybe',
                 'If you have a mental health issue, do you feel that it interferes with your work when NOT being treated effectively?_not applicable to me',
                 'Do you think that discussing a mental health disorder with your employer would have negative consequences?_no']


# Combine all lists into one
complete_selection = cov_selection + var_selection + pca_selection

# Count occurrences
feature_counts = Counter(complete_selection)

# Keep only features that occur more than once
filtered_features = [feature for feature, count in feature_counts.items() if count > 1]

print(filtered_features)
print(len(filtered_features))


# Convert to DataFrame for better visualization
#feature_counts_df = pd.DataFrame(filtered_features, columns=['Feature'])

# Print the result
#print(feature_counts_df)