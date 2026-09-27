# Copyright (c) 2026 ROKCT INTELLIGENCE (PTY) LTD
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

"""Display names and subject pathways for the FET subjects added beside the
original six. Same `pathway` block as the Grades R-9 syllabi
(`comes_from`, `leads_to`, `fet_subjects`): Grade 10 comes from the Grade 9
subject(s) named in GET_SOURCES.md's pathway table, Grades 11-12 from the
grade before, and Grade 12 leads to the NSC examination."""

LANGUAGE_NAMES = {
    "english": "English", "afrikaans": "Afrikaans", "isizulu": "isiZulu",
    "isixhosa": "isiXhosa", "isindebele": "isiNdebele", "sepedi": "Sepedi",
    "sesotho": "Sesotho", "setswana": "Setswana", "siswati": "siSwati",
    "tshivenda": "Tshivenda", "xitsonga": "Xitsonga",
}

SUBJECT_NAMES = {
    "life_sciences": "Life Sciences",
    "agricultural_sciences": "Agricultural Sciences",
    "history": "History",
    "business_studies": "Business Studies",
    "life_orientation": "Life Orientation",
    "computer_applications_technology": "Computer Applications Technology",
    "information_technology": "Information Technology",
    "tourism": "Tourism",
    "consumer_studies": "Consumer Studies",
    "engineering_graphics_and_design": "Engineering Graphics and Design",
    "visual_arts": "Visual Arts",
    "religion_studies": "Religion Studies",
}
for _key, _name in LANGUAGE_NAMES.items():
    SUBJECT_NAMES[f"{_key}_home_language"] = f"{_name} Home Language"
    SUBJECT_NAMES[f"{_key}_first_additional_language"] = f"{_name} First Additional Language"

# Grade 9 subject (and strand) each FET subject builds on.
GRADE9_ROOTS = {
    "life_sciences": ["Natural Sciences (Grade 9): Life and Living"],
    "agricultural_sciences": ["Natural Sciences (Grade 9): Life and Living, Matter and Materials",
                              "Economic and Management Sciences (Grade 9)"],
    "history": ["Social Sciences (Grade 9): History"],
    "business_studies": ["Economic and Management Sciences (Grade 9): Entrepreneurship"],
    "life_orientation": ["Life Orientation (Grade 9)"],
    "computer_applications_technology": ["Technology (Grade 9)"],
    "information_technology": ["Mathematics (Grade 9)", "Technology (Grade 9)"],
    "tourism": ["Social Sciences (Grade 9): Geography",
                "Economic and Management Sciences (Grade 9)"],
    "consumer_studies": ["Economic and Management Sciences (Grade 9)",
                         "Natural Sciences (Grade 9)", "Technology (Grade 9)"],
    "engineering_graphics_and_design": ["Technology (Grade 9)", "Mathematics (Grade 9)"],
    "visual_arts": ["Creative Arts (Grade 9): Visual Arts"],
    "religion_studies": ["Life Orientation (Grade 9)", "Social Sciences (Grade 9)"],
}
for _key, _name in LANGUAGE_NAMES.items():
    GRADE9_ROOTS[f"{_key}_home_language"] = [f"{_name} Home Language (Grade 9)"]
    GRADE9_ROOTS[f"{_key}_first_additional_language"] = [
        f"{_name} First Additional Language (Grade 9)"]


def _pathway(folder):
    name = SUBJECT_NAMES[folder]

    def block(grade):
        comes_from = GRADE9_ROOTS[folder] if grade == 10 else [f"{name} (Grade {grade - 1})"]
        leads_to = ([f"{name} (Grade {grade + 1})"] if grade < 12
                    else [f"{name} NSC examination (Grade 12)"])
        return {"comes_from": list(comes_from), "leads_to": leads_to, "fet_subjects": [name]}
    return block


PATHWAYS = {folder: _pathway(folder) for folder in SUBJECT_NAMES}
