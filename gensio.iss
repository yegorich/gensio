; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "Gensio"
#define MyAppVersion "2.8.0"
#define MyAppPublisher "Gensio"
#define MyAppURL "https://github.com/cminyard/gensio"
#define InstallDir "c:/msys64/home/cminyard/install/Gensio"
#define mingw64Dir "c:/msys64/ucrt64"

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{C3E36C5E-6F82-4284-A46F-9A5F58C68C56})
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
AllowNoIcons=yes
; Uncomment the following line to run in non administrative install mode (install for current user only.)
;PrivilegesRequired=lowest
PrivilegesRequiredOverridesAllowed=dialog
OutputDir=C:\msys64\home\cminyard
OutputBaseFilename=Gensio
Compression=lzma
SolidCompression=yes
WizardStyle=modern
ChangesEnvironment=true

[Files]
Source: "{#InstallDir}/bin/gensiot.exe"; DestDir: "{app}/bin"
Source: "{#InstallDir}/bin/gensio_pty_helper.exe"; DestDir: "{app}/bin"
Source: "{#InstallDir}/bin/gmdns.exe"; DestDir: "{app}/bin"
Source: "{#InstallDir}/bin/gsound.exe"; DestDir: "{app}/bin"
Source: "{#InstallDir}/bin/gtlssh.exe"; DestDir: "{app}/bin"
Source: "{#InstallDir}/bin/gtlssh-keygen.exe"; DestDir: "{app}/bin"
Source: "{#InstallDir}/bin/gtlsshd.exe"; DestDir: "{app}/bin"
Source: "{#InstallDir}/bin/libgensio_echo.dll"; DestDir: "{app}/bin"
Source: "{#InstallDir}/bin/libgensio_serialdev.dll"; DestDir: "{app}/bin"
Source: "{#InstallDir}/bin/libgensio_file.dll"; DestDir: "{app}/bin"
Source: "{#InstallDir}/bin/libgensio_sound.dll"; DestDir: "{app}/bin"
Source: "{#InstallDir}/bin/libgensio_keepopen.dll"; DestDir: "{app}/bin"
Source: "{#InstallDir}/bin/libgensio_ssl.dll"; DestDir: "{app}/bin"
Source: "{#InstallDir}/bin/libgensio_kiss.dll"; DestDir: "{app}/bin"
Source: "{#InstallDir}/bin/libgensio_stdio.dll"; DestDir: "{app}/bin"
Source: "{#InstallDir}/bin/libgensio_mdns.dll"; DestDir: "{app}/bin"
Source: "{#InstallDir}/bin/libgensio_telnet.dll"; DestDir: "{app}/bin"
Source: "{#InstallDir}/bin/libgensio_msgdelim.dll"; DestDir: "{app}/bin"
Source: "{#InstallDir}/bin/libgensio_trace.dll"; DestDir: "{app}/bin"
Source: "{#InstallDir}/bin/libgensio_mux.dll"; DestDir: "{app}/bin"
Source: "{#InstallDir}/bin/libgensio_udp.dll"; DestDir: "{app}/bin"
Source: "{#InstallDir}/bin/libgensio-6.dll"; DestDir: "{app}/bin"  
Source: "{#InstallDir}/bin/libgensio_net.dll"; DestDir: "{app}/bin"
Source: "{#InstallDir}/bin/libgensio_xlt.dll"; DestDir: "{app}/bin"
Source: "{#InstallDir}/bin/libgensio_afskmdm.dll"; DestDir: "{app}/bin"
Source: "{#InstallDir}/bin/libgensio_perf.dll"; DestDir: "{app}/bin"
Source: "{#InstallDir}/bin/libgensiocpp-6.dll"; DestDir: "{app}/bin"
Source: "{#InstallDir}/bin/libgensio_ax25.dll"; DestDir: "{app}/bin"
Source: "{#InstallDir}/bin/libgensio_pty.dll"; DestDir: "{app}/bin"
Source: "{#InstallDir}/bin/libgensiomdns-6.dll"; DestDir: "{app}/bin"
Source: "{#InstallDir}/bin/libgensio_certauth.dll"; DestDir: "{app}/bin"
Source: "{#InstallDir}/bin/libgensio_python_swig-6.dll"; DestDir: "{app}/bin"
Source: "{#InstallDir}/bin/libgensiomdnscpp-6.dll"; DestDir: "{app}/bin"
Source: "{#InstallDir}/bin/libgensio_cm108gpio.dll"; DestDir: "{app}/bin"
Source: "{#InstallDir}/bin/libgensio_ratelimit.dll"; DestDir: "{app}/bin"
Source: "{#InstallDir}/bin/libgensioosh-6.dll"; DestDir: "{app}/bin"
Source: "{#InstallDir}/bin/libgensio_conacc.dll"; DestDir: "{app}/bin"
Source: "{#InstallDir}/bin/libgensio_relpkt.dll"; DestDir: "{app}/bin"
Source: "{#InstallDir}/bin/libgensiooshcpp-6.dll"; DestDir: "{app}/bin"
Source: "{#InstallDir}/bin/libgensio_dummy.dll"; DestDir: "{app}/bin"
Source: "{#InstallDir}/bin/libgensio_script.dll"; DestDir: "{app}/bin"

Source: "{#mingw64Dir}/bin/libgcc_s_seh-1.dll"; DestDir: "{app}/bin"
Source: "{#mingw64Dir}/bin/libstdc++-6.dll"; DestDir: "{app}/bin"
Source: "{#mingw64Dir}/bin/libwinpthread-1.dll"; DestDir: "{app}/bin"
Source: "{#mingw64Dir}/bin/libcrypto-3-x64.dll"; DestDir: "{app}/bin"
Source: "{#mingw64Dir}/bin/libssl-3-x64.dll"; DestDir: "{app}/bin"
Source: "{#mingw64Dir}/bin/libpcreposix-0.dll"; DestDir: "{app}/bin"
Source: "{#mingw64Dir}/bin/libpcre-1.dll"; DestDir: "{app}/bin"

Source: "{#InstallDir}/lib/libgensio.dll.a"; DestDir: "{app}/lib"
Source: "{#InstallDir}/lib/libgensio.dll.a"; DestDir: "{app}/lib"; DestName: "gensio.lib"
Source: "{#InstallDir}/lib/libgensiocpp.dll.a"; DestDir: "{app}/lib"
Source: "{#InstallDir}/lib/libgensiocpp.dll.a"; DestDir: "{app}/lib"; DestName: "gensiocpp.lib"
Source: "{#InstallDir}/lib/libgensiomdnscpp.dll.a"; DestDir: "{app}/lib"
Source: "{#InstallDir}/lib/libgensiomdnscpp.dll.a"; DestDir: "{app}/lib"; DestName: "gensiomdnscpp.lib"
Source: "{#InstallDir}/lib/libgensiooshcpp.dll.a"; DestDir: "{app}/lib"
Source: "{#InstallDir}/lib/libgensiooshcpp.dll.a"; DestDir: "{app}/lib"; DestName: "gensiooshcpp.lib"
Source: "{#InstallDir}/lib/libgensio_python_swig.dll.a"; DestDir: "{app}/lib"
Source: "{#InstallDir}/lib/libgensiomdns.dll.a"; DestDir: "{app}/lib"
Source: "{#InstallDir}/lib/libgensiomdns.dll.a"; DestDir: "{app}/lib"; DestName: "gensiomdns.lib"
Source: "{#InstallDir}/lib/libgensioosh.dll.a"; DestDir: "{app}/lib"
Source: "{#InstallDir}/lib/libgensioosh.dll.a"; DestDir: "{app}/lib"; DestName: "gensioosh.lib"

Source: "{#InstallDir}/python3/_gensio.pyd"; DestDir: "{app}/python3"
Source: "{#InstallDir}/python3/_pygensio.pyd"; DestDir: "{app}/python3"
Source: "{#InstallDir}/python3/gensio.py"; DestDir: "{app}/python3"
Source: "{#InstallDir}/python3/pygensio.py"; DestDir: "{app}/python3"

Source: "{#InstallDir}/include/gensio/argvutils.h"; DestDir: "{app}/include/gensio"
Source: "{#InstallDir}/include/gensio/gensio_list.h"; DestDir: "{app}/include/gensio"
Source: "{#InstallDir}/include/gensio/gensio_unix.h"; DestDir: "{app}/include/gensio"
Source: "{#InstallDir}/include/gensio/gensio"; DestDir: "{app}/include/gensio"
Source: "{#InstallDir}/include/gensio/gensio_ll_fd.h"; DestDir: "{app}/include/gensio"
Source: "{#InstallDir}/include/gensio/gensio_utils.h"; DestDir: "{app}/include/gensio"
Source: "{#InstallDir}/include/gensio/gensio.h"; DestDir: "{app}/include/gensio"
Source: "{#InstallDir}/include/gensio/gensio_ll_gensio.h"; DestDir: "{app}/include/gensio"
Source: "{#InstallDir}/include/gensio/gensio_version.h"; DestDir: "{app}/include/gensio"
Source: "{#InstallDir}/include/gensio/gensio_acc_gensio.h"; DestDir: "{app}/include/gensio"
Source: "{#InstallDir}/include/gensio/gensio_mdns.h"; DestDir: "{app}/include/gensio"
Source: "{#InstallDir}/include/gensio/gensio_win.h"; DestDir: "{app}/include/gensio"
Source: "{#InstallDir}/include/gensio/gensio_addr.h"; DestDir: "{app}/include/gensio"
Source: "{#InstallDir}/include/gensio/gensio_os_funcs.h"; DestDir: "{app}/include/gensio"
Source: "{#InstallDir}/include/gensio/gensiomdns"; DestDir: "{app}/include/gensio"
Source: "{#InstallDir}/include/gensio/gensio_ax25_addr.h"; DestDir: "{app}/include/gensio"
Source: "{#InstallDir}/include/gensio/gensio_os_funcs_public.h"; DestDir: "{app}/include/gensio"
Source: "{#InstallDir}/include/gensio/gensioosh"; DestDir: "{app}/include/gensio"
Source: "{#InstallDir}/include/gensio/gensio_base.h"; DestDir: "{app}/include/gensio"
Source: "{#InstallDir}/include/gensio/gensio_osops.h"; DestDir: "{app}/include/gensio"
Source: "{#InstallDir}/include/gensio/gensioosh_dllvisibility"; DestDir: "{app}/include/gensio"
Source: "{#InstallDir}/include/gensio/gensio_buffer.h"; DestDir: "{app}/include/gensio"
Source: "{#InstallDir}/include/gensio/gensio_osops_addrinfo.h"; DestDir: "{app}/include/gensio"
Source: "{#InstallDir}/include/gensio/gensioosh_dllvisibility.h"; DestDir: "{app}/include/gensio"
Source: "{#InstallDir}/include/gensio/gensio_circbuf.h"; DestDir: "{app}/include/gensio"
Source: "{#InstallDir}/include/gensio/gensio_osops_env.h"; DestDir: "{app}/include/gensio"
Source: "{#InstallDir}/include/gensio/netif.h"; DestDir: "{app}/include/gensio"
Source: "{#InstallDir}/include/gensio/gensio_class.h"; DestDir: "{app}/include/gensio"
Source: "{#InstallDir}/include/gensio/gensio_osops_stdsock.h"; DestDir: "{app}/include/gensio"
Source: "{#InstallDir}/include/gensio/pygensio.h"; DestDir: "{app}/include/gensio"
Source: "{#InstallDir}/include/gensio/gensio_control.h"; DestDir: "{app}/include/gensio"
Source: "{#InstallDir}/include/gensio/gensio_selector.h"; DestDir: "{app}/include/gensio"
Source: "{#InstallDir}/include/gensio/selector.h"; DestDir: "{app}/include/gensio"
Source: "{#InstallDir}/include/gensio/gensio_deprecated.h"; DestDir: "{app}/include/gensio"
Source: "{#InstallDir}/include/gensio/gensio_swig.h"; DestDir: "{app}/include/gensio"
Source: "{#InstallDir}/include/gensio/sergensio.h"; DestDir: "{app}/include/gensio"
Source: "{#InstallDir}/include/gensio/gensio_dllvisibility"; DestDir: "{app}/include/gensio"
Source: "{#InstallDir}/include/gensio/gensio_swig.i"; DestDir: "{app}/include/gensio"
Source: "{#InstallDir}/include/gensio/sergensio_class.h"; DestDir: "{app}/include/gensio"
Source: "{#InstallDir}/include/gensio/gensio_dllvisibility.h"; DestDir: "{app}/include/gensio"
Source: "{#InstallDir}/include/gensio/gensio_time.h"; DestDir: "{app}/include/gensio"
Source: "{#InstallDir}/include/gensio/gensio_err.h"; DestDir: "{app}/include/gensio"
Source: "{#InstallDir}/include/gensio/gensio_types.h"; DestDir: "{app}/include/gensio"

[Dirs]
Name: "{app}/etc/gtlssh"

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Icons]
Name: "{group}\{cm:ProgramOnTheWeb,{#MyAppName}}"; Filename: "{#MyAppURL}"
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"

[Code]
const EnvironmentKey = 'SYSTEM\CurrentControlSet\Control\Session Manager\Environment';

procedure EnvAddPath(Path: string);
var
    Paths: string;
begin
    { Retrieve current path (use empty string if entry not exists) }
    if not RegQueryStringValue(HKEY_LOCAL_MACHINE, EnvironmentKey, 'Path', Paths)
    then Paths := '';

    { Skip if string already found in path }
    if Pos(';' + Uppercase(Path) + ';', ';' + Uppercase(Paths) + ';') > 0 then exit;

    { App string to the end of the path variable }
    Paths := Paths + ';'+ Path +';'

    { Overwrite (or create if missing) path environment variable }
    if RegWriteStringValue(HKEY_LOCAL_MACHINE, EnvironmentKey, 'Path', Paths)
    then Log(Format('The [%s] added to PATH: [%s]', [Path, Paths]))
    else Log(Format('Error while adding the [%s] to PATH: [%s]', [Path, Paths]));
end;

procedure EnvRemovePath(Path: string);
var
    Paths: string;
    P: Integer;
begin
    { Skip if registry entry not exists }
    if not RegQueryStringValue(HKEY_LOCAL_MACHINE, EnvironmentKey, 'Path', Paths) then
        exit;

    { Skip if string not found in path }
    P := Pos(';' + Uppercase(Path) + ';', ';' + Uppercase(Paths) + ';');
    if P = 0 then exit;

    { Update path variable }
    Delete(Paths, P - 1, Length(Path) + 1);

    { Overwrite path environment variable }
    if RegWriteStringValue(HKEY_LOCAL_MACHINE, EnvironmentKey, 'Path', Paths)
    then Log(Format('The [%s] removed from PATH: [%s]', [Path, Paths]))
    else Log(Format('Error while removing the [%s] from PATH: [%s]', [Path, Paths]));
end;

procedure CurStepChanged(CurStep: TSetupStep);
begin
    if CurStep = ssPostInstall
     then EnvAddPath(ExpandConstant('{app}/bin'));
end;

procedure CurUninstallStepChanged(CurUninstallStep: TUninstallStep);
begin
    if CurUninstallStep = usPostUninstall
    then EnvRemovePath(ExpandConstant('{app}/bin'));
end;
