import pypandoc
import os

# Define the main LaTeX file and output file
main_tex_file = r'D:\\OneDrive - University at Buffalo\\Resume_CV_CL\\Latex\\resume.tex'
output_docx_file = r'D:\\OneDrive - University at Buffalo\\Resume_CV_CL\\Latex\\resume.docx'

# Define the directory containing all the LaTeX files
input_dir = r'D:\\OneDrive - University at Buffalo\\Resume_CV_CL\\Latex\\'

# Collect all the LaTeX files to be included in the conversion
additional_files = [
    'src\\education.tex',
    'src\\experience.tex',
    'src\\extracurricular.tex',
    'src\\heading.tex',
    'src\\projects.tex',
    'src\\skills.tex'
]

# Construct the command to include all the files
extra_args = [
    '--include-in-header', os.path.join(input_dir, 'custom-commands.tex'),
    # '--include-in-header', os.path.join(input_dir, 'glyphtounicode.tex')
]
for file in additional_files:
    extra_args.extend(['--include-before-body', os.path.join(input_dir, file)])

# Convert LaTeX to DOCX
output = pypandoc.convert_file(main_tex_file, 'docx', outputfile=output_docx_file, extra_args=extra_args)

# Check if the conversion was successful
if output == "":
    print(f'Successfully converted {main_tex_file} to {output_docx_file}')
else:
    print('Error in conversion:', output)
