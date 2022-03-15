# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps  # pylint: disable=unused-import
# pylint: disable=line-too-long, too-many-lines

helps['backup'] = """
type: group
short-summary: Manage Azure Backups.
"""

helps['backup container'] = """
type: group
short-summary: Resource which houses items or applications to be protected.
"""

helps['backup container list'] = """
type: command
short-summary: List containers registered to a Recovery services vault.
examples:
  - name: List containers registered to a Recovery services vault. (autogenerated)
    text: az backup container list --resource-group MyResourceGroup --vault-name MyVault --backup-management-type AzureIaasVM
    crafted: true
"""

helps['backup container register'] = """
type: command
short-summary: Register a Resource to the given Recovery Services Vault.
examples:
  - name: This command allows Azure Backup to convert the 'Resource' to a 'Backup Container' which is then registered to the given Recovery services vault. The Azure Backup service can then discover workloads of the given workload type within this container to be protected later.
    text: az backup container register --resource-group MyResourceGroup --vault-name MyVault --resource-id MyResourceId --workload-type MSSQL --backup-management-type AzureWorkload --resource-id MyResourceID
"""

helps['backup container re-register'] = """
type: command
short-summary: Reset the registration details for a given container.
examples:
  - name: Reset the registration details for a given container. To be used only in error scenarios as specified here (https://docs.microsoft.com/azure/backup/backup-sql-server-azure-troubleshoot#re-registration-failures). Understand the failure symptoms and causes before attempting re-registration.
    text: az backup container re-register --resource-group MyResourceGroup --vault-name MyVault --container-name MyContainer --workload-type MSSQL --backup-management-type AzureWorkload --yes
"""

helps['backup container show'] = """
type: command
short-summary: Show details of a container registered to a Recovery services vault.
examples:
  - name: Show details of a container registered to a Recovery services vault. (autogenerated)
    text: az backup container show --name MyContainer --resource-group MyResourceGroup --vault-name MyVault
    crafted: true
"""

helps['backup container unregister'] = """
type: command
short-summary: Unregister a Backup Container to make the underlying 'resource' be protected by another vault.
examples:
  - name: If you are backing up Azure File shares, and want to clean-up, you need to delete backups for those shares and unregister the parent Azure Storage account.
    text: az backup container unregister --container-name MyContainer --resource-group MyResourceGroup --vault-name MyVault --backup-management-type AzureStorage
"""

helps['backup item'] = """
type: group
short-summary: An item which is already protected or backed up to an Azure Recovery services vault with an associated policy.
"""

helps['backup item list'] = """
type: command
short-summary: List all backed up items within a container.
examples:
  - name: List all backed up items within a container. (autogenerated)
    text: az backup item list --resource-group MyResourceGroup --vault-name MyVault
    crafted: true
"""

helps['backup item set-policy'] = """
type: command
short-summary: Update the policy associated with this item. Use this to change policies of the backup item.
examples:
  - name: Update the policy associated with this item. Use this to change policies of the backup item.
    text: az backup item set-policy --vault-name MyVault --resource-group MyResourceGroup --container-name MyContainer --name MyItem --policy-name MyPolicy --backup-management-type AzureIaasVM
"""

helps['backup item show'] = """
type: command
short-summary: Show details of a particular backed up item.
examples:
  - name: Show details of a particular backed up item. (autogenerated)
    text: az backup item show --container-name MyContainer --name MyBackedUpItem --resource-group MyResourceGroup --vault-name MyVault
    crafted: true
"""

helps['backup job'] = """
type: group
short-summary: Entity which contains details of the job.
"""

helps['backup job list'] = """
type: command
short-summary: List all backup jobs of a Recovery Services vault.
examples:
  - name: List all backup jobs of a Recovery Services vault
    text: az backup job list --resource-group MyResourceGroup --vault-name MyVault
    crafted: true
"""

helps['backup job show'] = """
type: command
short-summary: Show details of a particular job.
examples:
  - name: Show details of a particular job. (autogenerated)
    text: az backup job show --name MyJob --resource-group MyResourceGroup --vault-name MyVault
    crafted: true
"""

helps['backup job stop'] = """
type: command
short-summary: Suspend or terminate a currently running job.
examples:
  - name: Suspend or terminate a currently running job. (autogenerated)
    text: az backup job stop --name MyJob --resource-group MyResourceGroup --vault-name MyVault
    crafted: true
"""

helps['backup job wait'] = """
type: command
short-summary: Wait until either the job completes or the specified timeout value is reached.
examples:
  - name: Wait until either the job completes or the specified timeout value is reached
    text: az backup job wait --name MyJob --resource-group MyResourceGroup --vault-name MyVault
    crafted: true
"""

helps['backup policy'] = """
type: group
short-summary: A backup policy defines when you want to take a backup and for how long you would retain each backup copy.
"""

helps['backup policy delete'] = """
type: command
short-summary: Delete a backup policy which doesn't have any associated backup items.
examples:
  - name: Before you can delete a Backup protection policy, the policy must not have any associated Backup items. To associate another policy with a Backup item, use the backup item set-policy command.
    text: az backup policy delete --name MyBackupPolicy --resource-group MyResourceGroup --vault-name MyVault
"""

helps['backup policy get-default-for-vm'] = """
type: command
short-summary: Get the default policy with default values to backup a VM.
examples:
  - name: Get the default policy with default values to backup a VM. (autogenerated)
    text: az backup policy get-default-for-vm --resource-group MyResourceGroup --vault-name MyVault
    crafted: true
"""

helps['backup policy list'] = """
type: command
short-summary: List all policies for a Recovery services vault.
examples:
  - name: List all policies for a Recovery services vault. (autogenerated)
    text: az backup policy list --resource-group MyResourceGroup --vault-name MyVault
    crafted: true
"""

helps['backup policy list-associated-items'] = """
type: command
short-summary: List all items protected by a backup policy.
examples:
  - name: List all items protected by a backup policy
    text: az backup policy list-associated-items --name MyBackupPolicy --resource-group MyResourceGroup --vault-name MyVault --backup-management-type AzureIaasVM
    crafted: true
"""

helps['backup policy set'] = """
type: command
short-summary: Update the existing policy with the provided details.
examples:
  - name: Update the existing policy with the provided details. (autogenerated)
    text: az backup policy set --policy {policy} --resource-group MyResourceGroup --vault-name MyVault
    crafted: true
"""

helps['backup policy show'] = """
type: command
short-summary: Show details of a particular policy.
examples:
  - name: Show details of a particular policy
    text: az backup policy show --name MyBackupPolicy --resource-group MyResourceGroup --vault-name MyVault
    crafted: true
"""

helps['backup policy create'] = """
type: command
short-summary: Create a new policy for the given BackupManagementType and workloadType.
examples:
  - name: Create a new policy for the given BackupManagementType and workloadType.
    text: az backup policy create --policy {policy} --resource-group MyResourceGroup --vault-name MyVault --name MyPolicy --backup-management-type AzureStorage
"""

helps['backup protectable-item'] = """
type: group
short-summary: Manage the item which is yet to be protected or backed up to an Azure Recovery services vault with an associated policy.
"""

helps['backup protectable-item initialize'] = """
type: command
short-summary: Trigger the discovery of any unprotected items of the given workload type in the given container.
examples:
  - name: Trigger the discovery of any unprotected items of the given workload type in the given container. Use this command to manually discover new DBs and proceed to protect them.
    text: az backup protectable-item initialize --resource-group MyResourceGroup --vault-name MyVault --workload-type MSSQL --container-name MyContainer
"""

helps['backup protectable-item list'] = """
type: command
short-summary: Retrieve all protectable items within a certain container or across all registered containers.
examples:
  - name: Retrieve all protectable items within a certain container or across all registered containers. It consists of all the elements in the hierarchy of the application. Returns DBs and their upper tier entities like Instance, AvailabilityGroup etc.
    text: az backup protectable-item list --resource-group MyResourceGroup --vault-name MyVault --backup-management-type AzureWorkload --workload-type MSSQL --container-name MyContainer
"""

helps['backup protectable-item show'] = """
type: command
short-summary: Retrieve the specified protectable item within the given container.
examples:
  - name: Retrieve the specified protectable item within the given container.
    text: az backup protectable-item show --resource-group MyResourceGroup --vault-name MyVault --workload-type MSSQL --protectable-item-type SQLAG --name Name  --server-name MyServerName
"""

helps['backup protection'] = """
type: group
short-summary: Manage protection of your items, enable protection or disable it, or take on-demand backups.
"""

helps['backup protection backup-now'] = """
type: command
short-summary: Perform an on-demand backup of a backed up item.
examples:
  - name: Perform an on-demand backup of a backed up item. (autogenerated)
    text: az backup protection backup-now --container-name MyContainer --item-name MyItem --resource-group MyResourceGroup --retain-until 01-02-2018 --vault-name MyVault --backup-management-type AzureIaasVM
    crafted: true
"""

helps['backup protection check-vm'] = """
type: command
short-summary: Find out whether the virtual machine is protected or not. If protected, it returns the recovery services vault ID, otherwise it returns empty.
examples:
  - name: Find out whether the virtual machine is protected or not. If protected, it returns the recovery services vault ID, otherwise it returns empty. (autogenerated)
    text: az backup protection check-vm --resource-group MyResourceGroup --vm myVM
    crafted: true
"""

helps['backup protection disable'] = """
type: command
short-summary: Stop protecting a backed up item. Can retain the backed up data forever or choose to delete it.
examples:
  - name: Stop protecting a backed up item. Can retain the backed up data forever or choose to delete it. (autogenerated)
    text: az backup protection disable --container-name MyContainer --backup-management-type AzureIaasVM --delete-backup-data false --item-name MyItem --resource-group MyResourceGroup --vault-name MyVault --yes
    crafted: true
"""

helps['backup protection enable-for-vm'] = """
type: command
short-summary: Start protecting a previously unprotected Azure VM as per the specified policy to a Recovery services vault.
examples:
  - name: Start protecting a previously unprotected Azure VM as per the specified policy to a Recovery services vault. (autogenerated)
    text: az backup protection enable-for-vm --policy-name MyPolicy --resource-group MyResourceGroup --vault-name MyVault --vm myVM
    crafted: true
"""

helps['backup protection enable-for-azurefileshare'] = """
type: command
short-summary: Start protecting a previously unprotected Azure File share within an Azure Storage account as per the specified policy to a Recovery services vault.
examples:
  - name: Start protecting a previously unprotected Azure File share within an Azure Storage account as per the specified policy to a Recovery services vault. Provide the Azure File share name and the parent storage account name.
    text: az backup protection enable-for-azurefileshare --policy-name MyPolicy --resource-group MyResourceGroup --vault-name MyVault --storage-account MyStorageAccount --azure-file-share MyAzureFileShare
"""

helps['backup protection undelete'] = """
type: command
short-summary: Rehydrate an item from softdeleted state to stop protection with retained data state.
examples:
  - name: Rehydrate an item from softdeleted state to stop protection with retained data state.
    text: az backup protection undelete --container-name MyContainer --item-name MyItem --resource-group MyResourceGroup --vault-name MyVault --backup-management-type AzureIaasVM --workload-type VM
"""

helps['backup protection enable-for-azurewl'] = """
type: command
short-summary: Start protecting a previously unprotected workload within an Azure VM as per the specified policy to a Recovery services vault. Provide the workload details as a protectable item.
examples:
  - name: Start protecting a previously unprotected workload within an Azure VM as per the specified policy to a Recovery services vault. Provide the workload details as a protectable item.
    text: az backup protection enable-for-azurewl --policy-name MyPolicy --resource-group MyResourceGroup --vault-name MyVault --protectable-item-name ItemName --protectable-item-type SQLInstance --server-name Myserver --workload-type MSSQL
"""

helps['backup protection auto-enable-for-azurewl'] = """
type: command
short-summary: Automatically protect all existing unprotected DBs and any DB which will be added later with the given policy.
examples:
  - name: Automatically protect all existing unprotected DBs and any DB which will be added later with the given policy.  Azure backup service will then regularly scan auto-protected containers for any new DBs and automatically protect them.
    text: az backup protection auto-enable-for-azurewl --policy-name MyPolicy --resource-group MyResourceGroup --vault-name MyVault  --protectable-item-name ItemName --protectable-item-type SQLInstance --server-name Myserver --workload-type MSSQL
"""

helps['backup protection auto-disable-for-azurewl'] = """
type: command
short-summary: Disable auto-protection for the specified protectable item.
examples:
  - name: Disable auto-protection for the specified protectable item.
    text: az backup protection auto-disable-for-azurewl --resource-group MyResourceGroup --vault-name MyVault  --protectable-item-name ItemName --protectable-item-type SQLInstance --server-name Myserver --workload-type MSSQL
"""

helps['backup protection resume'] = """
type: command
short-summary: Resume backup for the associated backup item. Use this to change the policy associated with the backup item.
examples:
  - name: Resume backup for the associated backup item. Use this to change the policy associated with the backup item.
    text: az backup protection resume --vault-name MyVault --resource-group MyResourceGroup --container-name MyContainer --backup-management-type AzureIaasVM --item-name MyItem --policy-name MyPolicy
"""

helps['backup protection update-for-vm'] = """
type: command
short-summary: Update disk exclusion settings associated with a backed up VM item.
examples:
  - name: Update disk exclusion settings associated with a backed up VM item.
    text: az backup protection update-for-vm --vault-name MyVault --resource-group MyResourceGroup --container-name MyContainer --item-name MyItem --disk-list-setting exclude --diskslist 1
"""

helps['backup recoveryconfig'] = """
type: group
short-summary: Manage recovery configuration of an Azure workload backed up item.
"""

helps['backup recoveryconfig show'] = """
type: command
short-summary: Construct the recovery configuration of an Azure workload backed up item.
examples:
  - name: Construct the recovery configuration of an Azure workload backed up item. The configuration object stores all details such as the recovery mode, target destinations for the restore and application specific parameters like target physical paths for SQL.
    text: az backup recoveryconfig show --container-name MyContainer --item-name MyItem --resource-group MyResourceGroup --vault-name MyVault --restore-mode OriginalWorkloadRestore
"""

helps['backup recoverypoint'] = """
type: group
short-summary: A snapshot of data at that point-of-time, stored in Recovery Services Vault, from which you can restore information.
"""

helps['backup recoverypoint list'] = """
type: command
short-summary: List all recovery points of a backed up item.
examples:
  - name: List all recovery points of a backed up item. (autogenerated)
    text: az backup recoverypoint list --container-name MyContainer --backup-management-type AzureIaasVM --item-name MyItem --resource-group MyResourceGroup --vault-name MyVault
    crafted: true
"""

helps['backup recoverypoint move'] = """
type: command
short-summary: Move a particular recovery point of a backed up item from one tier to another tier.
examples:
  - name: Move a particular recovery point of a backed up item.
    text: az backup recoverypoint move --container-name MyContainer --backup-management-type AzureIaasVM --item-name MyItem --resource-group MyResourceGroup --vault-name MyVault --name RpId --source-tier SourceTier --destination-tier DestinationTier
"""

helps['backup recoverypoint show'] = """
type: command
short-summary: Shows details of a particular recovery point.
examples:
  - name: Shows details of a particular recovery point. (autogenerated)
    text: az backup recoverypoint show --container-name MyContainer --backup-management-type AzureIaasVM --item-name MyItem --name MyRecoveryPoint --resource-group MyResourceGroup --vault-name MyVault
    crafted: true
"""

helps['backup recoverypoint show-log-chain'] = """
type: command
short-summary: List the start and end points of the unbroken log chain(s) of the given backup item.
examples:
  - name: List the start and end points of the unbroken log chain(s) of the given backup item. Use it to determine whether the point-in-time, to which the user wants the DB to be restored, is valid or not.
    text: az backup recoverypoint show-log-chain --container-name MyContainer --backup-management-type AzureWorkload --item-name MyItem --resource-group MyResourceGroup --vault-name MyVault
"""

helps['backup restore'] = """
type: group
short-summary: Restore backed up items from recovery points in a Recovery Services vault.
"""

helps['backup restore files'] = """
type: group
short-summary: Gives access to all files of a recovery point.
"""

helps['backup restore files mount-rp'] = """
type: command
short-summary: Download a script which mounts files of a recovery point.
examples:
  - name: Download a script which mounts files of a recovery point. (autogenerated)
    text: az backup restore files mount-rp --container-name MyContainer --item-name MyItem --resource-group MyResourceGroup --rp-name MyRp --vault-name MyVault
    crafted: true
"""

helps['backup restore files unmount-rp'] = """
type: command
short-summary: Close access to the recovery point.
examples:
  - name: Close access to the recovery point. (autogenerated)
    text: az backup restore files unmount-rp --container-name MyContainer --item-name MyItem --resource-group MyResourceGroup --rp-name MyRp --vault-name MyVault
    crafted: true
"""

helps['backup restore restore-disks'] = """
type: command
short-summary: Restore disks of the backed VM from the specified recovery point.
examples:
  - name: Restore disks of the backed VM from the specified recovery point. (autogenerated)
    text: az backup restore restore-disks --container-name MyContainer --item-name MyItem --resource-group MyResourceGroup --rp-name MyRp --storage-account mystorageaccount --vault-name MyVault
    crafted: true
"""

helps['backup restore restore-azurefileshare'] = """
type: command
short-summary: Restore backed up Azure file shares to the same file-share or another file-share in registered storage accounts.
examples:
  - name: Restore backed up Azure file shares to the same file-share or another file-share in registered storage accounts.
    text: az backup restore restore-azurefileshare --resource-group MyResourceGroup --vault-name MyVault --container-name MyContainer --item-name MyItem --rp-name recoverypoint --resolve-conflict Overwrite --restore-mode OriginalLocation
"""

helps['backup restore restore-azurefiles'] = """
type: command
short-summary: Restore backed up Azure files within a file-share to the same file-share or another file-share in registered storage accounts.
examples:
  - name: Restore backed up Azure files within a file-share to the same file-share or another file-share in registered storage accounts.
    text: az backup restore restore-azurefiles --resource-group MyResourceGroup --vault-name MyVault --container-name MyContainer --item-name MyItem --rp-name recoverypoint --resolve-conflict Overwrite --restore-mode OriginalLocation --source-file-type File --source-file-path Filepath1 Filepath2
"""

helps['backup restore restore-azurewl'] = """
type: command
short-summary: Restore backed up Azure Workloads in a Recovery services vault to another registered container or to the same container.
examples:
  - name: Restore backed up Azure Workloads in a Recovery services vault to another registered container or to the same container.
    text: az backup restore restore-azurewl --resource-group MyResourceGroup --vault-name MyVault --recovery-config MyRecoveryConfig
"""

helps['backup vault'] = """
type: group
short-summary: Online storage entity in Azure used to hold data such as backup copies, recovery points and backup policies.
"""

helps['backup vault backup-properties'] = """
type: group
short-summary: Properties of the Recovery Services vault.
"""

helps['backup vault backup-properties set'] = """
type: command
short-summary: Sets backup related properties of the Recovery Services vault.
examples:
  - name: Sets backup related properties of the Recovery Services vault. (autogenerated)
    text: az backup vault backup-properties set --backup-storage-redundancy GeoRedundant --name MyRecoveryServicesVault --resource-group MyResourceGroup --subscription MySubscription
    crafted: true
"""

helps['backup vault backup-properties show'] = """
type: command
short-summary: Gets backup related properties of the Recovery Services vault.
examples:
  - name: Gets backup related properties of the Recovery Services vault. (autogenerated)
    text: az backup vault backup-properties show --name MyRecoveryServicesVault --resource-group MyResourceGroup
    crafted: true
"""

helps['backup vault create'] = """
type: command
short-summary: Create a new Recovery Services vault.
examples:
  - name: Create a new Recovery Services vault. (autogenerated)
    text: az backup vault create --location westus2 --name MyRecoveryServicesVault --resource-group MyResourceGroup
    crafted: true
"""

helps['backup vault delete'] = """
type: command
short-summary: Delete an existing Recovery services vault.
examples:
  - name: Delete an existing Recovery services vault. (autogenerated)
    text: az backup vault delete --name MyRecoveryServicesVault --resource-group MyResourceGroup --yes
    crafted: true
"""

helps['backup vault list'] = """
type: command
short-summary: List Recovery service vaults within a subscription.
"""

helps['backup vault show'] = """
type: command
short-summary: Show details of a particular Recovery service vault.
examples:
  - name: Show details of a particular Recovery service vault. (autogenerated)
    text: az backup vault show --name MyRecoveryServicesVault --resource-group MyResourceGroup
    crafted: true
"""
helps['backup vault identity'] = """
type: group
short-summary: Identity details of a Recovery Services Vault.
"""
helps['backup vault identity assign'] = """
type: command
short-summary: Assign Identities to Recovery Services vault.
examples:
  - name: Assign Identities to Recovery Services vault. (autogenerated)
    text: az backup vault identity assign --system-assigned --user-assigned MyIdentityId1 --resource-group MyResourceGroup --name MyVault
    crafted: true
"""
helps['backup vault identity remove'] = """
type: command
short-summary: Remove Identities of Recovery Services vault.
examples:
  - name: Remove Identities of Recovery Services vault. (autogenerated)
    text: az backup vault identity remove --system-assigned --user-assigned MyIdentityId1 --resource-group MyResourceGroup --name MyVault
    crafted: true
"""
helps['backup vault identity show'] = """
type: command
short-summary: Show Identities of Recovery Services vault.
examples:
  - name: Show Identities of Recovery Services vault. (autogenerated)
    text: az backup vault identity show --resource-group MyResourceGroup --name MyVault
    crafted: true
"""
helps['backup vault encryption'] = """
type: group
short-summary: Encryption details of a Recovery Services Vault.
"""
helps['backup vault encryption update'] = """
type: command
short-summary: Update encryption properties of a Recovery Services Vault.
examples:
  - name: Update encryption properties to use user assigned identity of a Recovery Services Vault.
    text: az backup vault encryption update --encryption-key-id MyEncryptionKeyId --mi-user-assigned MyUserAssignedIdentityId --resource-group MyResourceGroup --name MyVault
  - name: Update encryption properties to use system assigned identity of a Recovery Services Vault.
    text: az backup vault encryption update --encryption-key-id MyEncryptionKeyId --mi-system-assigned --resource-group MyResourceGroup --name MyVault
"""
helps['backup vault encryption show'] = """
type: command
short-summary: Show details of encryption properties of a Recovery Services Vault.
examples:
  - name: Show details of encryption properties of a Recovery Services Vault.
    text: az backup vault encryption show --resource-group MyResourceGroup --name MyVault
"""
